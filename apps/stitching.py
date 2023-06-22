import streamlit as st
import cv2
import numpy as np
from PIL import Image

import io


def app():
    @st.cache
    def stitch_images(image1, image2):
    # Convert the images to grayscale
      gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
      gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

      # Find the keypoints and descriptors using SIFT
      sift = cv2.SIFT_create()
      keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
      keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

      # Match the keypoints using a Brute-Force Matcher
      bf = cv2.BFMatcher()
      matches = bf.knnMatch(descriptors1, descriptors2, k=2)

      # Apply ratio test to filter out bad matches
      good_matches = []
      for m, n in matches:
          if m.distance < 0.75 * n.distance:
              good_matches.append(m)

      # Estimate the homography matrix using RANSAC
      if len(good_matches) > 4:
          src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
          dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
          H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

          # Warp image1 to image2 using the homography matrix
          height, width, channels = image2.shape
          warped_image1 = cv2.warpPerspective(image1, H, (width, height))

          # Merge image2 and warped image1
          merged_image = cv2.addWeighted(image2, 0.5, warped_image1, 0.5, 0)

          return merged_image
      else:
          return None
    

    st.title('Image Stitching')
    st.write('Upload two images to stitch them together.')
    image1 = st.file_uploader('Upload Image 1', type=['jpg', 'jpeg', 'png'])
    image2 = st.file_uploader('Upload Image 2', type=['jpg', 'jpeg', 'png'])
    if image1 and image2:
      image1_data = np.fromstring(image1.read(), np.uint8)
      image1 = cv2.imdecode(image1_data, cv2.IMREAD_COLOR)
      st.image(image1, channels='BGR', caption='Image 1', use_column_width=True)
      image2_data = np.fromstring(image2.read(), np.uint8)
      image2 = cv2.imdecode(image2_data, cv2.IMREAD_COLOR)
      st.image(image2, channels='BGR', caption='Image 2', use_column_width=True)
      if st.button('Stitch Images'):
          merged_image = stitch_images(image1, image2)
          if merged_image is not None:
              st.image(merged_image, channels='BGR', caption='Merged Image', use_column_width=True)
          else:
              st.write('Unable to stitch images. Please try again with different images.')
          image = Image.fromarray(merged_image)

        # Create a BytesIO object to store the image data
          image_bytes = io.BytesIO()

        # Save the image as bytes in the BytesIO object
          image.save(image_bytes, format='PNG')
          image_bytes.seek(0)  # Reset the file pointer to the beginning

        # Create a download button for the image
          st.download_button(
            label='Download Image',
            data=image_bytes,
            file_name='image.png',
            mime='image/png'
        )

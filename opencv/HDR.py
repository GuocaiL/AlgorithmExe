import cv2
import numpy as np

# 将曝光过的图像加载到列表
img_fn = ["img0.jpg", "img1.jpg", "img2.jpg", "img3.jpg","img4.jpg","img5.jpg","img6.jpg"]
img_list = [cv2.imread("photo/"+fn) for fn in img_fn]
exposure_times = np.array([16.0, 8.0, 4.0, 2.5,1.0,0.25,0.0333], dtype=np.float32)

# 将曝光合并到HDR图像
merge_debvec = cv2.createMergeDebevec()
hdr_debvec = merge_debvec.process(img_list, times=exposure_times.copy())
merge_robertson = cv2.createMergeRobertson()
hdr_robertson = merge_robertson.process(img_list, times=exposure_times.copy())

# HDR图像的色调映射
tonemap1 = cv2.createTonemapDurand(gamma=2.2)
res_debvec = tonemap1.process(hdr_debvec.copy())
tonemap2 = cv2.createTonemapDurand(gamma=1.3)
res_robertson = tonemap2.process(hdr_robertson.copy())

# 使用Mertens融合合并曝光
merge_mertens = cv2.createMergeMertens()
res_mertens = merge_mertens.process(img_list)

# 转换为8位整数并储存
res_debvec_8bit = np.clip(res_debvec * 255, 0, 255).astype('uint8')
res_robertson_8bit = np.clip(res_robertson * 255, 0, 255).astype('uint8')
res_mertens_8bit = np.clip(res_mertens * 255, 0, 255).astype('uint8')

cv2.imshow("ldr_debvec", res_debvec_8bit)
cv2.imshow("ldr_robertson", res_robertson_8bit)
cv2.imshow("fusion_mertens", res_mertens_8bit)

while 1:
    key = cv2.waitKey(1)
    if key > 0:
        break
cv2.destroyAllWindows()

import cv2

# 画像の読み込み
img1 = cv2.imread('./images/image1.jpg')
img2 = cv2.imread('./images/image2.jpg')

# スティッチャーの作成
stitcher = cv2.Stitcher.create()
#stitcher = cv2.Stitcher.create(mode=cv2.Stitcher_PANORAMA)
#stitcher = cv2.Stitcher.create(mode=cv2.Stitcher_SCANS)

# スティッチングの実行
(status, stitched) = stitcher.stitch([img1, img2])

# スティッチングが成功した場合
if status == cv2.Stitcher_OK:
    # スティッチングされた画像をファイルとして保存
    cv2.imwrite('stitched_image.jpg', stitched)
else:
    # スティッチングが失敗した場合
    print("Error during stitching: ", status)

# 調査用
#import code
#console = code.InteractiveConsole(locals=locals())
#console.interact()

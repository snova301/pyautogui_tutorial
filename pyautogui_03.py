import pyautogui
import numpy as np

def main():
    # スクリーンショットを撮影
    pyautogui.screenshot(region=(100, 700, 300, 300)).save('filename.png')
    
    # 'filename.png'と同じ画像をスクリーン上から探し左上の座標と幅、高さを返す
    loc_sc = pyautogui.locateOnScreen('filename.png')
    print(loc_sc)

    # 'filename.png'と同じ画像をスクリーン上から探し、中央の座標を返す
    loc_sc_cen = pyautogui.locateCenterOnScreen('filename.png')
    print(loc_sc_cen)

    # 'filename.png'と同じ画像をスクリーン上から複数個探し、リストで返す
    loc_all = pyautogui.locateAllOnScreen('filename.png')
    list_loc = [list(i) for i in list(loc_all)] # タプル形式なのでリストに変換
    print(list_loc)

    # numpy配列に変換
    np_loc = np.array(list_loc)
    print(np_loc)

    # locateAllOnScreen は中央の座標を返す関数がないので自作
    np_loc_cen_x = np_loc[:, 0] + np_loc[:, 2]/2
    np_loc_cen_y = np_loc[:, 1] + np_loc[:, 3]/2
    np_loc_cen = np.array([np_loc_cen_x, np_loc_cen_y]).T
    print(np_loc_cen)

if __name__ == '__main__':
    main()
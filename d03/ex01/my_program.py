#!/usr/bin/python3
# coding : utf8

from local_lib.path import Path

if __name__ == "__main__":
    d = Path('/tmp/yolo')
    d.mkdir_p()
    f = Path('/tmp/yolo/swag.gy')
    f.touch()
    f.open()
    f.write_text("YoloSwag")
    print(f.text())

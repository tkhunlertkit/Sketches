#!/usr/bin/python

import click
import time
import os, os.path
import mouse_listener as ml
import text

from config import (
    # pre-selection coordinates
    photo_icon_coordinate,
    gallery_tab_location,
    gallery_pull_down_icon,
    select_other_location,

    origin_coor_offset,

    # post-selection coordi,
    confirm_crop_location,
    corfirm_select_location,
    long_press_for_paste,
    paste_click_location,
    final_confirm,

    y_spacing,
    x_spacing,
    make_1_to_1,
    first_delay,
    long_press_wait,
    wait_between_each_click,
    num_columns,
    dir,
    wait_between_each_post,
    copy_text_filename,
    default_comment
)

def wait(second):
    time.sleep(second)

def count_files(dir):
    return len([filename for filename in os.listdir(dir)
        if os.path.isfile(os.path.join(dir, filename))
            and not filename.startswith('.')])

def get_coordinate(index):
    row = index / num_columns
    col = index - (row * num_columns)
    coorx = origin_coor_offset[0] + (col * x_spacing)
    coory = origin_coor_offset[1] + (row * y_spacing)
    return [coorx, coory]

if __name__ == '__main__':

    list_of_pre_selection = [
        photo_icon_coordinate,
        gallery_tab_location,
        gallery_pull_down_icon,
        select_other_location
    ]

    post_selection_before_long_press= [
        confirm_crop_location,
        corfirm_select_location
    ]

    after_long_pressed = [
        paste_click_location,
        final_confirm
    ]

    ml.start_mouse_listen('Click BlueStacks Window')
    wait(2)
    wait(first_delay)

    read_file = text.line_generator(copy_text_filename)
    for i in range(count_files(dir)):
        try:
            text.copy(next(read_file))
        except:
            text.copy(default_comment)


        print 'posting picture:', i + 1, 'with message'
        text.paste()
        print

        get_coordinate(i)

        for loc in list_of_pre_selection:
            click.mouseclick(*loc)
            wait(wait_between_each_click)

        # actual photo icon in select menu
        click.mouseclick(*get_coordinate(i))
        wait(wait_between_each_click)

        for loc in post_selection_before_long_press:
            click.mouseclick(*loc)
            wait(wait_between_each_click)

        click.long_click(long_press_for_paste[0], long_press_for_paste[1], long_press_wait)
        wait(0.5)

        for loc in after_long_pressed:
            click.mouseclick(*loc)
            wait(wait_between_each_click)

        wait(wait_between_each_post)

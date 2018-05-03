import mouse_listener as ml
import os.path

if __name__ == '__main__':
	if os.path.isfile('config.py'):
		import config
		try:
			dir = config.dir
		except AttributeError:
			dir = ''

	ml.start_mouse_listen('click BlueStacks window')
	with open('config.py', 'w') as f:

		f.write('# pre-selection coordinates\n')
		x, y = ml.start_mouse_listen('click photo icon')
		f.write('photo_icon_coordinate   = [%s, %s]\n' % (x, y))
		x, y = ml.start_mouse_listen('click gallery tab')
		f.write('gallery_tab_location    = [%s, %s]\n' % (x, y))
		x, y = ml.start_mouse_listen('click gallery pull down')
		f.write('gallery_pull_down_icon  = [%s, %s]\n' % (x, y))
		x, y = ml.start_mouse_listen('click select other')
		f.write('select_other_location   = [%s, %s]\n' % (x, y))

		x_orig, y_orig = ml.start_mouse_listen('click first picture')
		f.write('origin_coor_offset      = [%s, %s]\n' % (x_orig, y_orig))
		ml.start_mouse_listen('click back')
		ml.start_mouse_listen('click gallery pull down')
		ml.start_mouse_listen('click select other')
		x, y = ml.start_mouse_listen('click picture to the right of the first picture')
		f.write('x_spacing = %s\n' % (x - x_orig))
		ml.start_mouse_listen('click back')
		ml.start_mouse_listen('click gallery pull down')
		ml.start_mouse_listen('click select other')
		x, y = ml.start_mouse_listen('click picture below the first picture')
		f.write('y_spacing = %s\n' % (y - y_orig))

		f.write('\n# post-selection coordinates\n')
		x, y = ml.start_mouse_listen('click confirm for crop')
		f.write('confirm_crop_location   = [%s, %s]\n' % (x, y))
		x, y = ml.start_mouse_listen('click confirm select picture')
		f.write('corfirm_select_location = [%s, %s]\n' % (x, y))
		x, y = ml.start_mouse_listen('click text box to paste text')
		f.write('long_press_for_paste    = [%s, %s]\n' % (x, y))
		x, y = ml.start_mouse_listen('click paste')
		f.write('paste_click_location    = [%s, %s]\n' % (x, y))
		x, y = ml.start_mouse_listen('click confirm')
		f.write('final_confirm           = [%s, %s]\n' % (x, y))
		f.write('long_press_wait         = 1  # second\n\n')

		f.write('# Modifiable Stuff\n')
		f.write('first_delay             = 2  # second\n')
		f.write('wait_between_each_click = 10 # second\n')
		f.write('num_columns             = 7  # second\n')
		f.write('wait_between_each_post  = 10 # second\n\n')
		f.write('dir                     = \'%s\' # google drive directory\n' % dir)
		f.write('copy_text_filename      = \'copy_text.txt\' # google drive directory\n')
		f.write('default_comment         = \'\'\n')

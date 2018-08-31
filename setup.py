from setuptools import setup
setup(name='dui_test',
      version='1.0',
      license="GPL 2.0",
      description="Dials User Interface, pre - release Test",
      author='Luis Fuentes-Montero (Luiso)',
      author_email='luis.fuentes-montero@diamond.ac.uk',
      url='none yet',
      platforms='GNU/Linux & Mac OS',

      packages=['mini_idials_w_GUI', 'mini_idials_w_GUI.outputs_n_viewers'],
      data_files=[('mini_idials_w_GUI/resources', ['mini_idials_w_GUI/resources/DIALS_Logo_smaller_centred_grayed.png',
                                                   'mini_idials_w_GUI/resources/DIALS_Logo_smaller_centred.png',
                                                   'mini_idials_w_GUI/resources/find_spots_grayed.png',
                                                   'mini_idials_w_GUI/resources/find_spots.png',
                                                   'mini_idials_w_GUI/resources/import_grayed.png',
                                                   'mini_idials_w_GUI/resources/import.png',
                                                   'mini_idials_w_GUI/resources/index_grayed.png',
                                                   'mini_idials_w_GUI/resources/index.png',
                                                   'mini_idials_w_GUI/resources/integrate_grayed.png',
                                                   'mini_idials_w_GUI/resources/integrate.png',
                                                   'mini_idials_w_GUI/resources/refine_grayed.png',
                                                   'mini_idials_w_GUI/resources/refine.png',
                                                   'mini_idials_w_GUI/resources/reindex_grayed.png',
                                                   'mini_idials_w_GUI/resources/reindex.png',
                                                   'mini_idials_w_GUI/resources/re_try_grayed.png',
                                                   'mini_idials_w_GUI/resources/re_try.png',
                                                   'mini_idials_w_GUI/resources/stop_grayed.png',
                                                   'mini_idials_w_GUI/resources/stop.png',
                                                   'mini_idials_w_GUI/resources/zoom_plus_ico.png',
                                                   'mini_idials_w_GUI/resources/zoom_ono_one_ico.png',
                                                   'mini_idials_w_GUI/resources/zoom_minus_ico.png'])],
      entry_points={'console_scripts':['dui=mini_idials_w_GUI.main_dui:main']},
     )


to_remove = '''
                    'mini_idials_w_GUI/outputs_n_viewers/img_viewer_icons/zoom_plus_ico.png',
                    'mini_idials_w_GUI/outputs_n_viewers/img_viewer_icons/zoom_ono_one_ico.png',
                    'mini_idials_w_GUI/outputs_n_viewers/img_viewer_icons/zoom_minus_ico.png'])],
'''

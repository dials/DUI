'''
Containers for widgets related to each step

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
'''

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import os, sys

from params_live_gui_generator import PhilWidget
from simpler_param_widgets import FindspotsSimplerParameterTab, IndexSimplerParamTab, \
                                  RefineBravaiSimplerParamTab, RefineSimplerParamTab, \
                                  IntegrateSimplerParamTab

from dials.command_line.find_spots import phil_scope as phil_scope_find_spots
from dials.command_line.index import phil_scope as phil_scope_index

from dials.command_line.refine_bravais_settings import phil_scope as phil_scope_r_b_settings

from dials.command_line.refine import phil_scope as phil_scope_refine
from dials.command_line.integrate import phil_scope as phil_scope_integrate
from dials.command_line.export import phil_scope as phil_scope_export

def template_right_side_build(in_str_tmp, dir_path):

    expli_templ = True

    print "in_str_tmp =", in_str_tmp
    print "dir_path =", dir_path

    out_str = dir_path + in_str_tmp
    #lst_files = os.listdir(str(dir_path))     #<<< test comment

    for pos, single_char in reversed(list(enumerate(in_str_tmp))):
        if(single_char == "."):
            pos_sep = pos

    left_sd_name = in_str_tmp[:pos_sep]
    print "left_sd_name =", left_sd_name

    ext_name = in_str_tmp[pos_sep:]
    print "ext_name =", ext_name

    if(ext_name == ".h5"):
        print "found h5 file"
        expli_templ = False
        out_str = left_sd_name
        out_str = out_str + ext_name

    else:
        out_str = left_sd_name

        max_tail_size = int(len(in_str_tmp) / 3)
        print "max_tail_size =", max_tail_size
        for tail_size in xrange(max_tail_size):
            prev_str = out_str
            pos_to_replase = len(out_str) - tail_size - 1
            for num_char in '0123456789':
                if out_str[pos_to_replase] == num_char:
                    out_str = out_str[:pos_to_replase] + '#' + out_str[pos_to_replase + 1:]

            if(prev_str == out_str):
                #print "found non num char"
                break

        out_str = out_str + ext_name

    return out_str, expli_templ

def default_string(my_cmd):
    print "\n\n default_string(", my_cmd,"):"

    prev_char = None
    new_cmd = ""

    for single_char in my_cmd:

        if(single_char != "#"):
            new_cmd += single_char

        elif(prev_char != "#"):
            new_cmd += "*"

        prev_char = single_char

    print "new_cmd =", new_cmd

    print "\n\n"

    return new_cmd


def template_from_lst_build(in_str_lst):
    print "in_str_lst =", in_str_lst
    str_lst = []
    for single_qstring in in_str_lst:
        str_lst.append(str(single_qstring))

    print "str_lst =", str_lst

    out_str = ""
    for pos in xrange(len(str_lst[0])):
        all_equal = True
        single_char = str_lst[0][pos]
        for single_string in str_lst:
            try:
                if(single_string[pos] != single_char):
                    all_equal = False
            except:
                all_equal =False

        if(all_equal == True):
            out_str = out_str + single_char

        else:
            out_str = out_str + "#"

    print "out_str =", out_str

    return out_str

class LstFilesView(QTextEdit):

    refreshed = pyqtSignal(str)

    def __init__(self, parent = None):
        super(LstFilesView, self).__init__()
        print "\n\n __init__ from LstFilesView \n\n"
        self.textChanged.connect(self.refresh_me)

    def add_txt(self, str_to_print):

        #TODO reconcider how elegant is this
        try:
            self.append(str_to_print)

        except:
            self.append(str_to_print[0])


    def show_lst(self, lst):
        self.clear()
        for single_file in lst:
            self.add_txt(single_file)

        self.refresh_me()

    def refresh_me(self):
        all_text = self.toPlainText()
        self.refreshed.emit(all_text)

class ImportPage(QWidget):

    update_command_lst = pyqtSignal(list)

    '''
    This stacked widget basically helps the user to browse the input images
    path, there is no auto-generated GUI form Phil parameters in use withing
    this widget.
    '''

    def __init__(self, parent = None):
        super(ImportPage, self).__init__(parent = None)

        self.rb_group = QButtonGroup()

        template_grp =  QGroupBox(" Import from File(s) ")
        template_vbox =  QVBoxLayout()
        self.templ_lin =   QLineEdit(self)
        self.templ_lin.setText(" ? ")

        self.simple_lin =   QLineEdit(self)
        self.simple_lin.setText(" ? ")


        self.lst_view = LstFilesView()

        self.radbutt_simple = QRadioButton("Simple use of \"*\" for completeness")
        self.rb_group.addButton(self.radbutt_simple)
        self.radbutt_simple.clicked.connect(self.action_simple)

        self.radbutt_list = QRadioButton("Enter the entire list of files")
        self.rb_group.addButton(self.radbutt_list)
        self.radbutt_list.clicked.connect(self.action_list)

        self.radbutt_templ = QRadioButton("Use template syntax")
        self.rb_group.addButton(self.radbutt_templ)
        self.radbutt_templ.clicked.connect(self.action_template)

        opn_fil_btn = QPushButton("\n Select File(s)\n")
        tmp_hbox = QHBoxLayout()
        tmp_hbox.addStretch()
        tmp_hbox.addWidget(opn_fil_btn)
        template_vbox.addLayout(tmp_hbox)

        template_vbox.addWidget(self.radbutt_simple)
        template_vbox.addWidget(self.simple_lin)
        template_vbox.addWidget(self.radbutt_list)
        template_vbox.addWidget(self.lst_view)
        template_vbox.addWidget(self.radbutt_templ)


        template_vbox.addWidget(self.templ_lin)
        template_grp.setLayout(template_vbox)

        big_layout =  QVBoxLayout()
        big_layout.addWidget(template_grp)

        opn_fil_btn.clicked.connect(self.open_files)

        self.lst_view.refreshed.connect(self.list_changed)

        self.expli_templ = True
        self.setLayout(big_layout)
        self.show()

    def get_arg_obj(self, sys_arg_in):
        print "\n sys_arg_in =", sys_arg_in, "\n"
        if(sys_arg_in.template != None):
            str_arg = str(sys_arg_in.template)
            self.templ_lin.setText(str_arg)
            self.intro_file_changed(str_arg)

    def intro_file_changed(self, value = None):

        tml_ini = "template="
        str_value = str(value)

        tmp_off = '''
        if(self.expli_templ == True):
            my_cmd = tml_ini + str_value

        else:
            my_cmd = str_value
        self.command_lst = ["import", my_cmd]
        '''

        self.templ_cmd = str_value
        dfa_str = default_string(str_value)
        self.simple_lin.setText(dfa_str)

    def list_changed(self, list_obj = None):
        print "list_changed"
        self.path_new_lst = str(list_obj).split("\n")
        self.handle_lst_path(self.path_new_lst)
        self.check_radbut()

    def check_radbut(self):
        print "self.radbutt_simple.isChecked() =", self.radbutt_simple.isChecked()
        print "self.radbutt_list.isChecked() =", self.radbutt_list.isChecked()
        print "self.radbutt_templ.isChecked() =", self.radbutt_templ.isChecked()

        some_radbutt_is_checked = False
        if(self.radbutt_simple.isChecked()):
            self.action_simple()

        elif(self.radbutt_list.isChecked()):
            self.action_list()

        elif(self.radbutt_templ.isChecked()):
            self.action_template()

        else:
            self.action_simple()

    def action_simple(self):
        print "action_simple"
        self.command_lst = ["import", str(self.simple_lin.text())]
        self.update_command_lst.emit(self.command_lst)
        print "self.command_lst =", self.command_lst, "\n"

    def action_list(self):
        print "action_list"
        self.command_lst = ["import"]
        for single_file_path in self.path_new_lst:
            if(len(single_file_path) > 4):
                self.command_lst.append(single_file_path)

        self.update_command_lst.emit(self.command_lst)
        print "self.command_lst =", self.command_lst, "\n"

    def action_template(self):
        print "action_template"
        self.command_lst = ["import", "template=" + self.templ_cmd]
        self.update_command_lst.emit(self.command_lst)
        print "self.command_lst =", self.command_lst, "\n"

    def open_files(self):
        self.expli_templ = True

        print "from open_files  << import page >>"
        get_wor_dir = str(os.getcwd())
        print "\nget_wor_dir =", get_wor_dir, "\n"

        lst_file_path =  QFileDialog.getOpenFileNames(self, "Open File(s)",
                                                      get_wor_dir,
                                                      "All Files (*.*)")

        print "[ file path selected ] =", lst_file_path
        print "len(lst_file_path) =", len(lst_file_path)

        self.lst_view.show_lst(lst_file_path)

    def handle_lst_path(self, lst_file_path):
        for single_string in lst_file_path:
            print "single_string =", single_string

        if(lst_file_path and len(lst_file_path) == 1):
            selected_file_path = str(lst_file_path[0])

            print "\n selected_file_path =", selected_file_path, "\n"
            print "type(selected_file_path) =", type(selected_file_path)

            for pos, single_char in enumerate(selected_file_path):
                if(single_char == "/" or single_char == "\\"):
                    pos_sep = pos

            else:
                print "Failed to find dir path"
                return

            print "pos_sep =", pos_sep

            #TODO make this dir more persistent for the next time the user opens the dialog
            dir_name = selected_file_path[:pos_sep]
            if(dir_name[0:3] == "(u\'"):
                print "dir_name[0:3] == \"(u\'\""
                dir_name = dir_name[3:]

            print "\ndir_name(final) =", dir_name, "\n"

            templ_str_tmp = selected_file_path[pos_sep:]
            #print "templ_str_tmp =", templ_str_tmp

            templ_r_side, self.expli_templ = template_right_side_build(templ_str_tmp, dir_name)


            templ_str_final = dir_name + templ_r_side
            self.templ_lin.setText(templ_str_final)
            self.intro_file_changed(templ_str_final)

        elif(len(lst_file_path) > 1):
            print "time to handle multiple files selected"
            templ_str_final = template_from_lst_build(lst_file_path)
            self.templ_lin.setText(templ_str_final)
            self.intro_file_changed(templ_str_final)

        else:
            print "Failed to change file"


    def activate_me(self):
        self.templ_lin.setEnabled(True)

    def gray_me_out(self):
        self.templ_lin.setEnabled(False)

class ParamAdvancedWidget( QWidget):
    def __init__(self, phl_obj = None, parent = None):
        super(ParamAdvancedWidget, self).__init__()

        #self.super_parent = parent.super_parent
        #self.param_widget_parent = parent.param_widget_parent

        self.scrollable_widget = PhilWidget(phl_obj, parent = self)
        scrollArea = QScrollArea()
        scrollArea.setWidget(self.scrollable_widget)
        vbox =  QVBoxLayout()

        search_label = QLabel("search:")
        search_edit = QLineEdit("type search here")
        search_edit.textChanged.connect(self.scrollable_widget.user_searching)


        hbox = QHBoxLayout()
        hbox.addWidget(search_label)
        hbox.addWidget(search_edit)
        vbox.addLayout(hbox)

        vbox.addWidget(scrollArea)
        self.setLayout(vbox)
        self.show()

def update_lst_pair(lst_ini, str_path, str_value):
    new_lst = []
    found = False
    for pos, pair in enumerate(lst_ini):
        if(pair[0] == str_path):
            new_pair = [str_path, str_value]
            found = True

        else:
            new_pair = pair

        new_lst.append(new_pair)

    if(found == False):
        new_lst.append([str_path, str_value])

    return new_lst

def pair2string(str_path, str_value):
    str_out = str(str_path) + "=" + str(str_value)
    return str_out

def build_lst_str(cmd_0, lst_pair):
    lst_str = [cmd_0]
    for pair in lst_pair:
        str_cmd = pair2string(pair[0], pair[1])
        lst_str.append(str_cmd)

    return lst_str

def string2pair(str_in):
    pair = None
    for pos, single_char in enumerate(str_in):
        if(single_char == "="):
            eq_pos = pos
            pair = [str_in[0:pos], str_in[pos+1:]]
            return pair


def buils_lst_pair(lst_in):
    lst_pair = []
    for par_str in lst_in[1:len(lst_in)]:
        #print "par_str =", par_str
        pair = string2pair(par_str)
        #print "pair =", pair
        lst_pair.append(pair)

    return lst_pair

class ParamMainWidget( QWidget):

    update_command_lst = pyqtSignal(list)

    def __init__(self, phl_obj = None, simp_widg = None, parent = None, upper_label = None):
        super(ParamMainWidget, self).__init__()

        self.command_lst = [None]
        self.lst_pair = []

        try:
            self.my_phl_obj = phl_obj
            self.simp_widg_in = simp_widg
        except:
            print "\n\n\n something went wrong here wiht the phil object \n\n\n"



        #self.param_widget_parent = self

        self._vbox = QVBoxLayout()

        self.build_param_widget()

        self.reset_btn = QPushButton("Reset to Default", self)
        self.reset_btn.clicked.connect(self.reset_par)

        label_font = QFont()
        sys_font_point_size =  label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        self.step_label = QLabel(str(upper_label))
        self.step_label.setFont(label_font)

        self._vbox.addWidget(self.step_label)
        self._vbox.addWidget(self.dual_level_tab)
        self._vbox.addWidget(self.reset_btn)

        self.setLayout(self._vbox)
        self.show()

    def build_param_widget(self):
        self.dual_level_tab = QTabWidget()
        self.sipler_widget = self.simp_widg_in()
        self.advanced_widget = ParamAdvancedWidget(phl_obj = self.my_phl_obj, parent = self)
        self.advanced_widget.scrollable_widget.item_changed.connect(self.update_lin_txt)

        try:
            self.sipler_widget.item_changed.connect(self.update_advanced_widget)

        except:
            print "found self.sipler_widget without << item_changed >> signal"

        self.dual_level_tab.addTab(self.sipler_widget, "Simple")
        self.dual_level_tab.addTab(self.advanced_widget, "Advanced")

    def reset_par(self):
        print "Reseting"

        #TODO here is suposed to reset idials low level parameters to TODO
        for i in reversed(range(self._vbox.count())):
            widgetToRemove = self._vbox.itemAt( i ).widget()
            self._vbox.removeWidget( widgetToRemove )
            widgetToRemove.setParent( None )

        self.build_param_widget()

        self._vbox.addWidget(self.step_label)
        self._vbox.addWidget(self.dual_level_tab)
        self._vbox.addWidget(self.reset_btn)


        print "<< inner >>self.command_lst =", self.command_lst
        self.command_lst = [self.command_lst[0]]
        self.lst_pair = []
        print "<< inner >>self.command_lst =", self.command_lst



        self.update_command_lst.emit(self.command_lst)

        try:
            self.sipler_widget.set_max_nproc()
            print "\n Tunning nproc to maximum \n"

        except:
            print "\n This step runs as fas as it can with nproc = 1 \n"

        #TODO here is suposed to reset idials low level parameters to TODO

    def update_advanced_widget(self, str_path, str_value):

        for bg_widg in(self.advanced_widget.scrollable_widget.lst_var_widg ,
                       self.sipler_widget.lst_var_widg):
            for widg in bg_widg:
                try:
                    if(widg.local_path == str_path):
                        if(widg.tmp_lst == None):
                            try:
                                num_val = float(str_value)
                                widg.setValue(num_val)

                            except:
                                print "\n\n Type Mismatch while searching for twin parameter \n\n"

                        else:
                            for pos, val in enumerate(widg.tmp_lst):
                                if(val == str_value):
                                    print "found val, v=", val
                                    widg.setCurrentIndex(pos)

                except:
                    pass

    def update_simpler_widget(self, str_path, str_value):

        for widg in self.sipler_widget.lst_var_widg:
            try:
                if(widg.local_path == str_path):
                    print "found << widg.local_path == str_path >> "

                    try:
                        num_val = float(str_value)
                        widg.setValue(num_val)

                    except:
                        try:
                            for pos, val in enumerate(widg.tmp_lst):
                                if(val == str_value):
                                    print "found val, v=", val
                                    widg.setCurrentIndex(pos)

                        except:
                            print "\n\n Type Mismatch in simpler_param_widgets \n\n"

            except:
                print "skip label_str"


    def update_lin_txt(self, str_path, str_value):
        cmd_to_run = str_path + "=" + str_value
        self.update_advanced_widget(str_path, str_value)
        self.update_simpler_widget(str_path, str_value)

        self.lst_pair = update_lst_pair(self.lst_pair, str_path, str_value)
        self.command_lst = build_lst_str(self.command_lst[0], self.lst_pair)
        self.update_command_lst.emit(self.command_lst)

    def update_param(self, lst_in):
        self.reset_par()
        if(len(lst_in) > 1):
            new_lst_pair = buils_lst_pair(lst_in)
            self.lst_pair = new_lst_pair
            self.command_lst = build_lst_str(self.command_lst[0], self.lst_pair)

            for pair in self.lst_pair:
                self.update_advanced_widget(pair[0], pair[1])
        else:
            self.lst_pair = []
            self.command_lst = [self.command_lst[0]]

    def gray_me_out(self):
        self.reset_btn.setEnabled(False)
        palt_gray = QPalette()
        palt_gray.setColor(QPalette.WindowText, QColor(88, 88, 88, 88))
        for bg_widg in(self.advanced_widget.scrollable_widget.lst_var_widg ,
                       self.advanced_widget.scrollable_widget.lst_label_widg,
                       self.sipler_widget.lst_var_widg):

            for widg in bg_widg:
                widg.setStyleSheet("color: rgba(88, 88, 88, 88)")

                try:
                    widg.setEnabled(False)

                except:
                    pass

    def activate_me(self):
        self.reset_btn.setEnabled(True)
        for bg_widg in(self.advanced_widget.scrollable_widget.lst_var_widg ,
                       self.advanced_widget.scrollable_widget.lst_label_widg,
                       self.sipler_widget.lst_var_widg):

            for widg in bg_widg:

                widg.setStyleSheet("color: rgba(0, 0, 0, 255)")
                try:
                    widg.setStyleSheet(widg.style_orign)
                except:
                    pass

                try:
                    widg.setEnabled(True)

                except:
                    pass

class ParamWidget(QWidget):

    update_command_lst = pyqtSignal(list)

    def __init__(self, label_str):
        super(ParamWidget, self).__init__()
        self.my_label = label_str

        inner_widgs = {
                       "find_spots":              [phil_scope_find_spots   , FindspotsSimplerParameterTab ],
                       "index"     :              [phil_scope_index        , IndexSimplerParamTab         ],
                       "refine_bravais_settings": [phil_scope_r_b_settings , RefineBravaiSimplerParamTab  ],
                       "refine"    :              [phil_scope_refine       , RefineSimplerParamTab        ],
                       "integrate" :              [phil_scope_integrate    , IntegrateSimplerParamTab     ],
                        }

        if(label_str == "import"):
            #self.my_widget = TmpImportWidget()
            self.my_widget = ImportPage()


        else:
            self.my_widget = ParamMainWidget(phl_obj = inner_widgs[label_str][0],
                                             simp_widg = inner_widgs[label_str][1],
                                             parent = self, upper_label = label_str)

        self.my_widget.command_lst = [label_str]

        self.my_widget.update_command_lst.connect(self.update_parent_lst)

        v_left_box =  QVBoxLayout()
        v_left_box.addWidget(self.my_widget)
        self.setLayout(v_left_box)
        self.show()

    def update_param(self, curr_step):
        self.my_widget.update_param(curr_step.command_lst)

    def update_parent_lst(self, command_lst):
        self.update_command_lst.emit(command_lst)

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    #ex = ParamWidget("find_spots")
    ex = ParamWidget("import")
    sys.exit(app.exec_())



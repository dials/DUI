import sys
#PyQt4_ver = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "using PyQt4"
#'''
PySide_ver = '''
from PySide.QtGui import *
from PySide.QtCore import *
pyqtSignal = Signal
print "using PySide"
#'''


class inner_widg( QWidget):
    item_changed = pyqtSignal()
    def __init__(self, parent):
        super(inner_widg, self).__init__()
        bg_box =  QVBoxLayout(self)


        label_tst = QLabel("indexing")
        label_tst.setFont(QFont("Monospace", 14, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_nproc =  QHBoxLayout()
        label_nproc = QLabel("        nproc")
        label_nproc.setFont(QFont("Times",16, QFont.Bold))
        hbox_nproc.addWidget(label_nproc)

        spn_box_nproc = QSpinBox()
        spn_box_nproc.local_path = "dummy path"
        spn_box_nproc.valueChanged.connect(self.spnbox_changed)

        hbox_nproc.addWidget(spn_box_nproc)
        bg_box.addLayout(hbox_nproc)
        hbox_discover_better_experimental_model =  QHBoxLayout()
        label_discover_better_experimental_model = QLabel("        discover_better_experimental_model")
        label_discover_better_experimental_model.setFont(QFont("Times",16, QFont.Bold))
        hbox_discover_better_experimental_model.addWidget(label_discover_better_experimental_model)

        spn_box_discover_better_experimental_model = QComboBox()
        spn_box_discover_better_experimental_model.tmp_lst=[]
        spn_box_discover_better_experimental_model.tmp_lst.append("True")
        spn_box_discover_better_experimental_model.tmp_lst.append("False")
        for lst_itm in spn_box_discover_better_experimental_model.tmp_lst:
            spn_box_discover_better_experimental_model.addItem(lst_itm)
        spn_box_discover_better_experimental_model.currentIndexChanged.connect(self.combobox_changed)

        hbox_discover_better_experimental_model.addWidget(spn_box_discover_better_experimental_model)
        bg_box.addLayout(hbox_discover_better_experimental_model)
        hbox_mm_search_scope =  QHBoxLayout()
        label_mm_search_scope = QLabel("        mm_search_scope")
        label_mm_search_scope.setFont(QFont("Times",16, QFont.Bold))
        hbox_mm_search_scope.addWidget(label_mm_search_scope)

        spn_box_mm_search_scope = QDoubleSpinBox()
        spn_box_mm_search_scope.local_path = "dummy path"
        spn_box_mm_search_scope.valueChanged.connect(self.spnbox_changed)

        hbox_mm_search_scope.addWidget(spn_box_mm_search_scope)
        bg_box.addLayout(hbox_mm_search_scope)
        hbox_wide_search_binning =  QHBoxLayout()
        label_wide_search_binning = QLabel("        wide_search_binning")
        label_wide_search_binning.setFont(QFont("Times",16, QFont.Bold))
        hbox_wide_search_binning.addWidget(label_wide_search_binning)

        spn_box_wide_search_binning = QDoubleSpinBox()
        spn_box_wide_search_binning.local_path = "dummy path"
        spn_box_wide_search_binning.valueChanged.connect(self.spnbox_changed)

        hbox_wide_search_binning.addWidget(spn_box_wide_search_binning)
        bg_box.addLayout(hbox_wide_search_binning)
        hbox_min_cell =  QHBoxLayout()
        label_min_cell = QLabel("        min_cell")
        label_min_cell.setFont(QFont("Times",16, QFont.Bold))
        hbox_min_cell.addWidget(label_min_cell)

        spn_box_min_cell = QDoubleSpinBox()
        spn_box_min_cell.local_path = "dummy path"
        spn_box_min_cell.valueChanged.connect(self.spnbox_changed)

        hbox_min_cell.addWidget(spn_box_min_cell)
        bg_box.addLayout(hbox_min_cell)
        hbox_max_cell =  QHBoxLayout()
        label_max_cell = QLabel("        max_cell")
        label_max_cell.setFont(QFont("Times",16, QFont.Bold))
        hbox_max_cell.addWidget(label_max_cell)

        spn_box_max_cell = QDoubleSpinBox()
        spn_box_max_cell.local_path = "dummy path"
        spn_box_max_cell.valueChanged.connect(self.spnbox_changed)

        hbox_max_cell.addWidget(spn_box_max_cell)
        bg_box.addLayout(hbox_max_cell)
        hbox_max_cell_multiplier =  QHBoxLayout()
        label_max_cell_multiplier = QLabel("        max_cell_multiplier")
        label_max_cell_multiplier.setFont(QFont("Times",16, QFont.Bold))
        hbox_max_cell_multiplier.addWidget(label_max_cell_multiplier)

        spn_box_max_cell_multiplier = QDoubleSpinBox()
        spn_box_max_cell_multiplier.local_path = "dummy path"
        spn_box_max_cell_multiplier.valueChanged.connect(self.spnbox_changed)

        hbox_max_cell_multiplier.addWidget(spn_box_max_cell_multiplier)
        bg_box.addLayout(hbox_max_cell_multiplier)
        hbox_nearest_neighbor_percentile =  QHBoxLayout()
        label_nearest_neighbor_percentile = QLabel("        nearest_neighbor_percentile")
        label_nearest_neighbor_percentile.setFont(QFont("Times",16, QFont.Bold))
        hbox_nearest_neighbor_percentile.addWidget(label_nearest_neighbor_percentile)

        spn_box_nearest_neighbor_percentile = QDoubleSpinBox()
        spn_box_nearest_neighbor_percentile.local_path = "dummy path"
        spn_box_nearest_neighbor_percentile.valueChanged.connect(self.spnbox_changed)

        hbox_nearest_neighbor_percentile.addWidget(spn_box_nearest_neighbor_percentile)
        bg_box.addLayout(hbox_nearest_neighbor_percentile)
        hbox_filter_ice =  QHBoxLayout()
        label_filter_ice = QLabel("        filter_ice")
        label_filter_ice.setFont(QFont("Times",16, QFont.Bold))
        hbox_filter_ice.addWidget(label_filter_ice)

        spn_box_filter_ice = QComboBox()
        spn_box_filter_ice.tmp_lst=[]
        spn_box_filter_ice.tmp_lst.append("True")
        spn_box_filter_ice.tmp_lst.append("False")
        for lst_itm in spn_box_filter_ice.tmp_lst:
            spn_box_filter_ice.addItem(lst_itm)
        spn_box_filter_ice.currentIndexChanged.connect(self.combobox_changed)

        hbox_filter_ice.addWidget(spn_box_filter_ice)
        bg_box.addLayout(hbox_filter_ice)
        label_tst = QLabel("    fft3d")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_peak_search =  QHBoxLayout()
        label_peak_search = QLabel("                peak_search")
        label_peak_search.setFont(QFont("Times",15, QFont.Bold))
        hbox_peak_search.addWidget(label_peak_search)

        spn_box_peak_search = QComboBox()
        spn_box_peak_search.tmp_lst=[]
        spn_box_peak_search.tmp_lst.append("*flood_fill")
        spn_box_peak_search.tmp_lst.append("clean")
        for lst_itm in spn_box_peak_search.tmp_lst:
            spn_box_peak_search.addItem(lst_itm)
        spn_box_peak_search.currentIndexChanged.connect(self.combobox_changed)

        hbox_peak_search.addWidget(spn_box_peak_search)
        bg_box.addLayout(hbox_peak_search)
        hbox_peak_volume_cutoff =  QHBoxLayout()
        label_peak_volume_cutoff = QLabel("                peak_volume_cutoff")
        label_peak_volume_cutoff.setFont(QFont("Times",15, QFont.Bold))
        hbox_peak_volume_cutoff.addWidget(label_peak_volume_cutoff)

        spn_box_peak_volume_cutoff = QDoubleSpinBox()
        spn_box_peak_volume_cutoff.local_path = "dummy path"
        spn_box_peak_volume_cutoff.valueChanged.connect(self.spnbox_changed)

        hbox_peak_volume_cutoff.addWidget(spn_box_peak_volume_cutoff)
        bg_box.addLayout(hbox_peak_volume_cutoff)
        label_tst = QLabel("        reciprocal_space_grid")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_n_points =  QHBoxLayout()
        label_n_points = QLabel("                        n_points")
        label_n_points.setFont(QFont("Times",14, QFont.Bold))
        hbox_n_points.addWidget(label_n_points)

        spn_box_n_points = QSpinBox()
        spn_box_n_points.local_path = "dummy path"
        spn_box_n_points.valueChanged.connect(self.spnbox_changed)

        hbox_n_points.addWidget(spn_box_n_points)
        bg_box.addLayout(hbox_n_points)
        hbox_d_min =  QHBoxLayout()
        label_d_min = QLabel("                        d_min")
        label_d_min.setFont(QFont("Times",14, QFont.Bold))
        hbox_d_min.addWidget(label_d_min)

        spn_box_d_min = QDoubleSpinBox()
        spn_box_d_min.local_path = "dummy path"
        spn_box_d_min.valueChanged.connect(self.spnbox_changed)

        hbox_d_min.addWidget(spn_box_d_min)
        bg_box.addLayout(hbox_d_min)
        hbox_sigma_phi_deg =  QHBoxLayout()
        label_sigma_phi_deg = QLabel("        sigma_phi_deg")
        label_sigma_phi_deg.setFont(QFont("Times",16, QFont.Bold))
        hbox_sigma_phi_deg.addWidget(label_sigma_phi_deg)

        spn_box_sigma_phi_deg = QDoubleSpinBox()
        spn_box_sigma_phi_deg.local_path = "dummy path"
        spn_box_sigma_phi_deg.valueChanged.connect(self.spnbox_changed)

        hbox_sigma_phi_deg.addWidget(spn_box_sigma_phi_deg)
        bg_box.addLayout(hbox_sigma_phi_deg)
        hbox_b_iso =  QHBoxLayout()
        label_b_iso = QLabel("        b_iso")
        label_b_iso.setFont(QFont("Times",16, QFont.Bold))
        hbox_b_iso.addWidget(label_b_iso)

        spn_box_b_iso = QDoubleSpinBox()
        spn_box_b_iso.local_path = "dummy path"
        spn_box_b_iso.valueChanged.connect(self.spnbox_changed)

        hbox_b_iso.addWidget(spn_box_b_iso)
        bg_box.addLayout(hbox_b_iso)
        hbox_rmsd_cutoff =  QHBoxLayout()
        label_rmsd_cutoff = QLabel("        rmsd_cutoff")
        label_rmsd_cutoff.setFont(QFont("Times",16, QFont.Bold))
        hbox_rmsd_cutoff.addWidget(label_rmsd_cutoff)

        spn_box_rmsd_cutoff = QDoubleSpinBox()
        spn_box_rmsd_cutoff.local_path = "dummy path"
        spn_box_rmsd_cutoff.valueChanged.connect(self.spnbox_changed)

        hbox_rmsd_cutoff.addWidget(spn_box_rmsd_cutoff)
        bg_box.addLayout(hbox_rmsd_cutoff)
        hbox_scan_range =  QHBoxLayout()
        label_scan_range = QLabel("        scan_range")
        label_scan_range.setFont(QFont("Times",16, QFont.Bold))
        hbox_scan_range.addWidget(label_scan_range)
        label_tst = QLabel("    known_symmetry")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_space_group =  QHBoxLayout()
        label_space_group = QLabel("                space_group")
        label_space_group.setFont(QFont("Times",15, QFont.Bold))
        hbox_space_group.addWidget(label_space_group)
        hbox_unit_cell =  QHBoxLayout()
        label_unit_cell = QLabel("                unit_cell")
        label_unit_cell.setFont(QFont("Times",15, QFont.Bold))
        hbox_unit_cell.addWidget(label_unit_cell)
        hbox_relative_length_tolerance =  QHBoxLayout()
        label_relative_length_tolerance = QLabel("                relative_length_tolerance")
        label_relative_length_tolerance.setFont(QFont("Times",15, QFont.Bold))
        hbox_relative_length_tolerance.addWidget(label_relative_length_tolerance)

        spn_box_relative_length_tolerance = QDoubleSpinBox()
        spn_box_relative_length_tolerance.local_path = "dummy path"
        spn_box_relative_length_tolerance.valueChanged.connect(self.spnbox_changed)

        hbox_relative_length_tolerance.addWidget(spn_box_relative_length_tolerance)
        bg_box.addLayout(hbox_relative_length_tolerance)
        hbox_absolute_angle_tolerance =  QHBoxLayout()
        label_absolute_angle_tolerance = QLabel("                absolute_angle_tolerance")
        label_absolute_angle_tolerance.setFont(QFont("Times",15, QFont.Bold))
        hbox_absolute_angle_tolerance.addWidget(label_absolute_angle_tolerance)

        spn_box_absolute_angle_tolerance = QDoubleSpinBox()
        spn_box_absolute_angle_tolerance.local_path = "dummy path"
        spn_box_absolute_angle_tolerance.valueChanged.connect(self.spnbox_changed)

        hbox_absolute_angle_tolerance.addWidget(spn_box_absolute_angle_tolerance)
        bg_box.addLayout(hbox_absolute_angle_tolerance)
        hbox_max_delta =  QHBoxLayout()
        label_max_delta = QLabel("                max_delta")
        label_max_delta.setFont(QFont("Times",15, QFont.Bold))
        hbox_max_delta.addWidget(label_max_delta)

        spn_box_max_delta = QDoubleSpinBox()
        spn_box_max_delta.local_path = "dummy path"
        spn_box_max_delta.valueChanged.connect(self.spnbox_changed)

        hbox_max_delta.addWidget(spn_box_max_delta)
        bg_box.addLayout(hbox_max_delta)
        label_tst = QLabel("    basis_vector_combinations")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_max_try =  QHBoxLayout()
        label_max_try = QLabel("                max_try")
        label_max_try.setFont(QFont("Times",15, QFont.Bold))
        hbox_max_try.addWidget(label_max_try)

        spn_box_max_try = QSpinBox()
        spn_box_max_try.local_path = "dummy path"
        spn_box_max_try.valueChanged.connect(self.spnbox_changed)

        hbox_max_try.addWidget(spn_box_max_try)
        bg_box.addLayout(hbox_max_try)
        hbox_solution_scorer =  QHBoxLayout()
        label_solution_scorer = QLabel("                solution_scorer")
        label_solution_scorer.setFont(QFont("Times",15, QFont.Bold))
        hbox_solution_scorer.addWidget(label_solution_scorer)

        spn_box_solution_scorer = QComboBox()
        spn_box_solution_scorer.tmp_lst=[]
        spn_box_solution_scorer.tmp_lst.append("filter")
        spn_box_solution_scorer.tmp_lst.append("*weighted")
        for lst_itm in spn_box_solution_scorer.tmp_lst:
            spn_box_solution_scorer.addItem(lst_itm)
        spn_box_solution_scorer.currentIndexChanged.connect(self.combobox_changed)

        hbox_solution_scorer.addWidget(spn_box_solution_scorer)
        bg_box.addLayout(hbox_solution_scorer)
        label_tst = QLabel("        filter")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_check_doubled_cell =  QHBoxLayout()
        label_check_doubled_cell = QLabel("                        check_doubled_cell")
        label_check_doubled_cell.setFont(QFont("Times",14, QFont.Bold))
        hbox_check_doubled_cell.addWidget(label_check_doubled_cell)

        spn_box_check_doubled_cell = QComboBox()
        spn_box_check_doubled_cell.tmp_lst=[]
        spn_box_check_doubled_cell.tmp_lst.append("True")
        spn_box_check_doubled_cell.tmp_lst.append("False")
        for lst_itm in spn_box_check_doubled_cell.tmp_lst:
            spn_box_check_doubled_cell.addItem(lst_itm)
        spn_box_check_doubled_cell.currentIndexChanged.connect(self.combobox_changed)

        hbox_check_doubled_cell.addWidget(spn_box_check_doubled_cell)
        bg_box.addLayout(hbox_check_doubled_cell)
        hbox_likelihood_cutoff =  QHBoxLayout()
        label_likelihood_cutoff = QLabel("                        likelihood_cutoff")
        label_likelihood_cutoff.setFont(QFont("Times",14, QFont.Bold))
        hbox_likelihood_cutoff.addWidget(label_likelihood_cutoff)

        spn_box_likelihood_cutoff = QDoubleSpinBox()
        spn_box_likelihood_cutoff.local_path = "dummy path"
        spn_box_likelihood_cutoff.valueChanged.connect(self.spnbox_changed)

        hbox_likelihood_cutoff.addWidget(spn_box_likelihood_cutoff)
        bg_box.addLayout(hbox_likelihood_cutoff)
        hbox_volume_cutoff =  QHBoxLayout()
        label_volume_cutoff = QLabel("                        volume_cutoff")
        label_volume_cutoff.setFont(QFont("Times",14, QFont.Bold))
        hbox_volume_cutoff.addWidget(label_volume_cutoff)

        spn_box_volume_cutoff = QDoubleSpinBox()
        spn_box_volume_cutoff.local_path = "dummy path"
        spn_box_volume_cutoff.valueChanged.connect(self.spnbox_changed)

        hbox_volume_cutoff.addWidget(spn_box_volume_cutoff)
        bg_box.addLayout(hbox_volume_cutoff)
        hbox_n_indexed_cutoff =  QHBoxLayout()
        label_n_indexed_cutoff = QLabel("                        n_indexed_cutoff")
        label_n_indexed_cutoff.setFont(QFont("Times",14, QFont.Bold))
        hbox_n_indexed_cutoff.addWidget(label_n_indexed_cutoff)

        spn_box_n_indexed_cutoff = QDoubleSpinBox()
        spn_box_n_indexed_cutoff.local_path = "dummy path"
        spn_box_n_indexed_cutoff.valueChanged.connect(self.spnbox_changed)

        hbox_n_indexed_cutoff.addWidget(spn_box_n_indexed_cutoff)
        bg_box.addLayout(hbox_n_indexed_cutoff)
        label_tst = QLabel("        weighted")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_power =  QHBoxLayout()
        label_power = QLabel("                        power")
        label_power.setFont(QFont("Times",14, QFont.Bold))
        hbox_power.addWidget(label_power)

        spn_box_power = QSpinBox()
        spn_box_power.local_path = "dummy path"
        spn_box_power.valueChanged.connect(self.spnbox_changed)

        hbox_power.addWidget(spn_box_power)
        bg_box.addLayout(hbox_power)
        hbox_volume_weight =  QHBoxLayout()
        label_volume_weight = QLabel("                        volume_weight")
        label_volume_weight.setFont(QFont("Times",14, QFont.Bold))
        hbox_volume_weight.addWidget(label_volume_weight)

        spn_box_volume_weight = QDoubleSpinBox()
        spn_box_volume_weight.local_path = "dummy path"
        spn_box_volume_weight.valueChanged.connect(self.spnbox_changed)

        hbox_volume_weight.addWidget(spn_box_volume_weight)
        bg_box.addLayout(hbox_volume_weight)
        hbox_n_indexed_weight =  QHBoxLayout()
        label_n_indexed_weight = QLabel("                        n_indexed_weight")
        label_n_indexed_weight.setFont(QFont("Times",14, QFont.Bold))
        hbox_n_indexed_weight.addWidget(label_n_indexed_weight)

        spn_box_n_indexed_weight = QDoubleSpinBox()
        spn_box_n_indexed_weight.local_path = "dummy path"
        spn_box_n_indexed_weight.valueChanged.connect(self.spnbox_changed)

        hbox_n_indexed_weight.addWidget(spn_box_n_indexed_weight)
        bg_box.addLayout(hbox_n_indexed_weight)
        hbox_rmsd_weight =  QHBoxLayout()
        label_rmsd_weight = QLabel("                        rmsd_weight")
        label_rmsd_weight.setFont(QFont("Times",14, QFont.Bold))
        hbox_rmsd_weight.addWidget(label_rmsd_weight)

        spn_box_rmsd_weight = QDoubleSpinBox()
        spn_box_rmsd_weight.local_path = "dummy path"
        spn_box_rmsd_weight.valueChanged.connect(self.spnbox_changed)

        hbox_rmsd_weight.addWidget(spn_box_rmsd_weight)
        bg_box.addLayout(hbox_rmsd_weight)
        label_tst = QLabel("    index_assignment")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_method =  QHBoxLayout()
        label_method = QLabel("                method")
        label_method.setFont(QFont("Times",15, QFont.Bold))
        hbox_method.addWidget(label_method)

        spn_box_method = QComboBox()
        spn_box_method.tmp_lst=[]
        spn_box_method.tmp_lst.append("*simple")
        spn_box_method.tmp_lst.append("local")
        for lst_itm in spn_box_method.tmp_lst:
            spn_box_method.addItem(lst_itm)
        spn_box_method.currentIndexChanged.connect(self.combobox_changed)

        hbox_method.addWidget(spn_box_method)
        bg_box.addLayout(hbox_method)
        label_tst = QLabel("        simple")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_hkl_tolerance =  QHBoxLayout()
        label_hkl_tolerance = QLabel("                        hkl_tolerance")
        label_hkl_tolerance.setFont(QFont("Times",14, QFont.Bold))
        hbox_hkl_tolerance.addWidget(label_hkl_tolerance)

        spn_box_hkl_tolerance = QDoubleSpinBox()
        spn_box_hkl_tolerance.local_path = "dummy path"
        spn_box_hkl_tolerance.valueChanged.connect(self.spnbox_changed)

        hbox_hkl_tolerance.addWidget(spn_box_hkl_tolerance)
        bg_box.addLayout(hbox_hkl_tolerance)
        label_tst = QLabel("        local")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_epsilon =  QHBoxLayout()
        label_epsilon = QLabel("                        epsilon")
        label_epsilon.setFont(QFont("Times",14, QFont.Bold))
        hbox_epsilon.addWidget(label_epsilon)

        spn_box_epsilon = QDoubleSpinBox()
        spn_box_epsilon.local_path = "dummy path"
        spn_box_epsilon.valueChanged.connect(self.spnbox_changed)

        hbox_epsilon.addWidget(spn_box_epsilon)
        bg_box.addLayout(hbox_epsilon)
        hbox_delta =  QHBoxLayout()
        label_delta = QLabel("                        delta")
        label_delta.setFont(QFont("Times",14, QFont.Bold))
        hbox_delta.addWidget(label_delta)

        spn_box_delta = QSpinBox()
        spn_box_delta.local_path = "dummy path"
        spn_box_delta.valueChanged.connect(self.spnbox_changed)

        hbox_delta.addWidget(spn_box_delta)
        bg_box.addLayout(hbox_delta)
        hbox_l_min =  QHBoxLayout()
        label_l_min = QLabel("                        l_min")
        label_l_min.setFont(QFont("Times",14, QFont.Bold))
        hbox_l_min.addWidget(label_l_min)

        spn_box_l_min = QDoubleSpinBox()
        spn_box_l_min.local_path = "dummy path"
        spn_box_l_min.valueChanged.connect(self.spnbox_changed)

        hbox_l_min.addWidget(spn_box_l_min)
        bg_box.addLayout(hbox_l_min)
        hbox_nearest_neighbours =  QHBoxLayout()
        label_nearest_neighbours = QLabel("                        nearest_neighbours")
        label_nearest_neighbours.setFont(QFont("Times",14, QFont.Bold))
        hbox_nearest_neighbours.addWidget(label_nearest_neighbours)

        spn_box_nearest_neighbours = QSpinBox()
        spn_box_nearest_neighbours.local_path = "dummy path"
        spn_box_nearest_neighbours.valueChanged.connect(self.spnbox_changed)

        hbox_nearest_neighbours.addWidget(spn_box_nearest_neighbours)
        bg_box.addLayout(hbox_nearest_neighbours)
        hbox_optimise_initial_basis_vectors =  QHBoxLayout()
        label_optimise_initial_basis_vectors = QLabel("        optimise_initial_basis_vectors")
        label_optimise_initial_basis_vectors.setFont(QFont("Times",16, QFont.Bold))
        hbox_optimise_initial_basis_vectors.addWidget(label_optimise_initial_basis_vectors)

        spn_box_optimise_initial_basis_vectors = QComboBox()
        spn_box_optimise_initial_basis_vectors.tmp_lst=[]
        spn_box_optimise_initial_basis_vectors.tmp_lst.append("True")
        spn_box_optimise_initial_basis_vectors.tmp_lst.append("False")
        for lst_itm in spn_box_optimise_initial_basis_vectors.tmp_lst:
            spn_box_optimise_initial_basis_vectors.addItem(lst_itm)
        spn_box_optimise_initial_basis_vectors.currentIndexChanged.connect(self.combobox_changed)

        hbox_optimise_initial_basis_vectors.addWidget(spn_box_optimise_initial_basis_vectors)
        bg_box.addLayout(hbox_optimise_initial_basis_vectors)
        hbox_debug =  QHBoxLayout()
        label_debug = QLabel("        debug")
        label_debug.setFont(QFont("Times",16, QFont.Bold))
        hbox_debug.addWidget(label_debug)

        spn_box_debug = QComboBox()
        spn_box_debug.tmp_lst=[]
        spn_box_debug.tmp_lst.append("True")
        spn_box_debug.tmp_lst.append("False")
        for lst_itm in spn_box_debug.tmp_lst:
            spn_box_debug.addItem(lst_itm)
        spn_box_debug.currentIndexChanged.connect(self.combobox_changed)

        hbox_debug.addWidget(spn_box_debug)
        bg_box.addLayout(hbox_debug)
        hbox_debug_plots =  QHBoxLayout()
        label_debug_plots = QLabel("        debug_plots")
        label_debug_plots.setFont(QFont("Times",16, QFont.Bold))
        hbox_debug_plots.addWidget(label_debug_plots)

        spn_box_debug_plots = QComboBox()
        spn_box_debug_plots.tmp_lst=[]
        spn_box_debug_plots.tmp_lst.append("True")
        spn_box_debug_plots.tmp_lst.append("False")
        for lst_itm in spn_box_debug_plots.tmp_lst:
            spn_box_debug_plots.addItem(lst_itm)
        spn_box_debug_plots.currentIndexChanged.connect(self.combobox_changed)

        hbox_debug_plots.addWidget(spn_box_debug_plots)
        bg_box.addLayout(hbox_debug_plots)
        hbox_combine_scans =  QHBoxLayout()
        label_combine_scans = QLabel("        combine_scans")
        label_combine_scans.setFont(QFont("Times",16, QFont.Bold))
        hbox_combine_scans.addWidget(label_combine_scans)

        spn_box_combine_scans = QComboBox()
        spn_box_combine_scans.tmp_lst=[]
        spn_box_combine_scans.tmp_lst.append("True")
        spn_box_combine_scans.tmp_lst.append("False")
        for lst_itm in spn_box_combine_scans.tmp_lst:
            spn_box_combine_scans.addItem(lst_itm)
        spn_box_combine_scans.currentIndexChanged.connect(self.combobox_changed)

        hbox_combine_scans.addWidget(spn_box_combine_scans)
        bg_box.addLayout(hbox_combine_scans)
        label_tst = QLabel("    refinement_protocol")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_n_macro_cycles =  QHBoxLayout()
        label_n_macro_cycles = QLabel("                n_macro_cycles")
        label_n_macro_cycles.setFont(QFont("Times",15, QFont.Bold))
        hbox_n_macro_cycles.addWidget(label_n_macro_cycles)

        spn_box_n_macro_cycles = QSpinBox()
        spn_box_n_macro_cycles.local_path = "dummy path"
        spn_box_n_macro_cycles.valueChanged.connect(self.spnbox_changed)

        hbox_n_macro_cycles.addWidget(spn_box_n_macro_cycles)
        bg_box.addLayout(hbox_n_macro_cycles)
        hbox_d_min_step =  QHBoxLayout()
        label_d_min_step = QLabel("                d_min_step")
        label_d_min_step.setFont(QFont("Times",15, QFont.Bold))
        hbox_d_min_step.addWidget(label_d_min_step)

        spn_box_d_min_step = QDoubleSpinBox()
        spn_box_d_min_step.local_path = "dummy path"
        spn_box_d_min_step.valueChanged.connect(self.spnbox_changed)

        hbox_d_min_step.addWidget(spn_box_d_min_step)
        bg_box.addLayout(hbox_d_min_step)
        hbox_d_min_start =  QHBoxLayout()
        label_d_min_start = QLabel("                d_min_start")
        label_d_min_start.setFont(QFont("Times",15, QFont.Bold))
        hbox_d_min_start.addWidget(label_d_min_start)

        spn_box_d_min_start = QDoubleSpinBox()
        spn_box_d_min_start.local_path = "dummy path"
        spn_box_d_min_start.valueChanged.connect(self.spnbox_changed)

        hbox_d_min_start.addWidget(spn_box_d_min_start)
        bg_box.addLayout(hbox_d_min_start)
        hbox_d_min_final =  QHBoxLayout()
        label_d_min_final = QLabel("                d_min_final")
        label_d_min_final.setFont(QFont("Times",15, QFont.Bold))
        hbox_d_min_final.addWidget(label_d_min_final)

        spn_box_d_min_final = QDoubleSpinBox()
        spn_box_d_min_final.local_path = "dummy path"
        spn_box_d_min_final.valueChanged.connect(self.spnbox_changed)

        hbox_d_min_final.addWidget(spn_box_d_min_final)
        bg_box.addLayout(hbox_d_min_final)
        hbox_verbosity =  QHBoxLayout()
        label_verbosity = QLabel("                verbosity")
        label_verbosity.setFont(QFont("Times",15, QFont.Bold))
        hbox_verbosity.addWidget(label_verbosity)

        spn_box_verbosity = QSpinBox()
        spn_box_verbosity.local_path = "dummy path"
        spn_box_verbosity.valueChanged.connect(self.spnbox_changed)

        hbox_verbosity.addWidget(spn_box_verbosity)
        bg_box.addLayout(hbox_verbosity)
        hbox_disable_unit_cell_volume_sanity_check =  QHBoxLayout()
        label_disable_unit_cell_volume_sanity_check = QLabel("                disable_unit_cell_volume_sanity_check")
        label_disable_unit_cell_volume_sanity_check.setFont(QFont("Times",15, QFont.Bold))
        hbox_disable_unit_cell_volume_sanity_check.addWidget(label_disable_unit_cell_volume_sanity_check)

        spn_box_disable_unit_cell_volume_sanity_check = QComboBox()
        spn_box_disable_unit_cell_volume_sanity_check.tmp_lst=[]
        spn_box_disable_unit_cell_volume_sanity_check.tmp_lst.append("True")
        spn_box_disable_unit_cell_volume_sanity_check.tmp_lst.append("False")
        for lst_itm in spn_box_disable_unit_cell_volume_sanity_check.tmp_lst:
            spn_box_disable_unit_cell_volume_sanity_check.addItem(lst_itm)
        spn_box_disable_unit_cell_volume_sanity_check.currentIndexChanged.connect(self.combobox_changed)

        hbox_disable_unit_cell_volume_sanity_check.addWidget(spn_box_disable_unit_cell_volume_sanity_check)
        bg_box.addLayout(hbox_disable_unit_cell_volume_sanity_check)
        label_tst = QLabel("        outlier_rejection")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_maximum_spot_error =  QHBoxLayout()
        label_maximum_spot_error = QLabel("                        maximum_spot_error")
        label_maximum_spot_error.setFont(QFont("Times",14, QFont.Bold))
        hbox_maximum_spot_error.addWidget(label_maximum_spot_error)

        spn_box_maximum_spot_error = QDoubleSpinBox()
        spn_box_maximum_spot_error.local_path = "dummy path"
        spn_box_maximum_spot_error.valueChanged.connect(self.spnbox_changed)

        hbox_maximum_spot_error.addWidget(spn_box_maximum_spot_error)
        bg_box.addLayout(hbox_maximum_spot_error)
        hbox_maximum_phi_error =  QHBoxLayout()
        label_maximum_phi_error = QLabel("                        maximum_phi_error")
        label_maximum_phi_error.setFont(QFont("Times",14, QFont.Bold))
        hbox_maximum_phi_error.addWidget(label_maximum_phi_error)

        spn_box_maximum_phi_error = QDoubleSpinBox()
        spn_box_maximum_phi_error.local_path = "dummy path"
        spn_box_maximum_phi_error.valueChanged.connect(self.spnbox_changed)

        hbox_maximum_phi_error.addWidget(spn_box_maximum_phi_error)
        bg_box.addLayout(hbox_maximum_phi_error)
        hbox_method =  QHBoxLayout()
        label_method = QLabel("        method")
        label_method.setFont(QFont("Times",16, QFont.Bold))
        hbox_method.addWidget(label_method)

        spn_box_method = QComboBox()
        spn_box_method.tmp_lst=[]
        spn_box_method.tmp_lst.append("*fft3d")
        spn_box_method.tmp_lst.append("fft1d")
        spn_box_method.tmp_lst.append("real_space_grid_search")
        for lst_itm in spn_box_method.tmp_lst:
            spn_box_method.addItem(lst_itm)
        spn_box_method.currentIndexChanged.connect(self.combobox_changed)

        hbox_method.addWidget(spn_box_method)
        bg_box.addLayout(hbox_method)
        label_tst = QLabel("    multiple_lattice_search")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_cluster_analysis_search =  QHBoxLayout()
        label_cluster_analysis_search = QLabel("                cluster_analysis_search")
        label_cluster_analysis_search.setFont(QFont("Times",15, QFont.Bold))
        hbox_cluster_analysis_search.addWidget(label_cluster_analysis_search)

        spn_box_cluster_analysis_search = QComboBox()
        spn_box_cluster_analysis_search.tmp_lst=[]
        spn_box_cluster_analysis_search.tmp_lst.append("True")
        spn_box_cluster_analysis_search.tmp_lst.append("False")
        for lst_itm in spn_box_cluster_analysis_search.tmp_lst:
            spn_box_cluster_analysis_search.addItem(lst_itm)
        spn_box_cluster_analysis_search.currentIndexChanged.connect(self.combobox_changed)

        hbox_cluster_analysis_search.addWidget(spn_box_cluster_analysis_search)
        bg_box.addLayout(hbox_cluster_analysis_search)
        hbox_recycle_unindexed_reflections =  QHBoxLayout()
        label_recycle_unindexed_reflections = QLabel("                recycle_unindexed_reflections")
        label_recycle_unindexed_reflections.setFont(QFont("Times",15, QFont.Bold))
        hbox_recycle_unindexed_reflections.addWidget(label_recycle_unindexed_reflections)

        spn_box_recycle_unindexed_reflections = QComboBox()
        spn_box_recycle_unindexed_reflections.tmp_lst=[]
        spn_box_recycle_unindexed_reflections.tmp_lst.append("True")
        spn_box_recycle_unindexed_reflections.tmp_lst.append("False")
        for lst_itm in spn_box_recycle_unindexed_reflections.tmp_lst:
            spn_box_recycle_unindexed_reflections.addItem(lst_itm)
        spn_box_recycle_unindexed_reflections.currentIndexChanged.connect(self.combobox_changed)

        hbox_recycle_unindexed_reflections.addWidget(spn_box_recycle_unindexed_reflections)
        bg_box.addLayout(hbox_recycle_unindexed_reflections)
        hbox_recycle_unindexed_reflections_cutoff =  QHBoxLayout()
        label_recycle_unindexed_reflections_cutoff = QLabel("                recycle_unindexed_reflections_cutoff")
        label_recycle_unindexed_reflections_cutoff.setFont(QFont("Times",15, QFont.Bold))
        hbox_recycle_unindexed_reflections_cutoff.addWidget(label_recycle_unindexed_reflections_cutoff)

        spn_box_recycle_unindexed_reflections_cutoff = QDoubleSpinBox()
        spn_box_recycle_unindexed_reflections_cutoff.local_path = "dummy path"
        spn_box_recycle_unindexed_reflections_cutoff.valueChanged.connect(self.spnbox_changed)

        hbox_recycle_unindexed_reflections_cutoff.addWidget(spn_box_recycle_unindexed_reflections_cutoff)
        bg_box.addLayout(hbox_recycle_unindexed_reflections_cutoff)
        hbox_minimum_angular_separation =  QHBoxLayout()
        label_minimum_angular_separation = QLabel("                minimum_angular_separation")
        label_minimum_angular_separation.setFont(QFont("Times",15, QFont.Bold))
        hbox_minimum_angular_separation.addWidget(label_minimum_angular_separation)

        spn_box_minimum_angular_separation = QDoubleSpinBox()
        spn_box_minimum_angular_separation.local_path = "dummy path"
        spn_box_minimum_angular_separation.valueChanged.connect(self.spnbox_changed)

        hbox_minimum_angular_separation.addWidget(spn_box_minimum_angular_separation)
        bg_box.addLayout(hbox_minimum_angular_separation)
        hbox_max_lattices =  QHBoxLayout()
        label_max_lattices = QLabel("                max_lattices")
        label_max_lattices.setFont(QFont("Times",15, QFont.Bold))
        hbox_max_lattices.addWidget(label_max_lattices)

        spn_box_max_lattices = QSpinBox()
        spn_box_max_lattices.local_path = "dummy path"
        spn_box_max_lattices.valueChanged.connect(self.spnbox_changed)

        hbox_max_lattices.addWidget(spn_box_max_lattices)
        bg_box.addLayout(hbox_max_lattices)
        label_tst = QLabel("        cluster_analysis")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_method =  QHBoxLayout()
        label_method = QLabel("                        method")
        label_method.setFont(QFont("Times",14, QFont.Bold))
        hbox_method.addWidget(label_method)

        spn_box_method = QComboBox()
        spn_box_method.tmp_lst=[]
        spn_box_method.tmp_lst.append("*dbscan")
        spn_box_method.tmp_lst.append("hcluster")
        for lst_itm in spn_box_method.tmp_lst:
            spn_box_method.addItem(lst_itm)
        spn_box_method.currentIndexChanged.connect(self.combobox_changed)

        hbox_method.addWidget(spn_box_method)
        bg_box.addLayout(hbox_method)
        label_tst = QLabel("            hcluster")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        label_tst = QLabel("                linkage")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_method =  QHBoxLayout()
        label_method = QLabel("                                        method")
        label_method.setFont(QFont("Times",14, QFont.Bold))
        hbox_method.addWidget(label_method)

        spn_box_method = QComboBox()
        spn_box_method.tmp_lst=[]
        spn_box_method.tmp_lst.append("*ward")
        for lst_itm in spn_box_method.tmp_lst:
            spn_box_method.addItem(lst_itm)
        spn_box_method.currentIndexChanged.connect(self.combobox_changed)

        hbox_method.addWidget(spn_box_method)
        bg_box.addLayout(hbox_method)
        hbox_metric =  QHBoxLayout()
        label_metric = QLabel("                                        metric")
        label_metric.setFont(QFont("Times",14, QFont.Bold))
        hbox_metric.addWidget(label_metric)

        spn_box_metric = QComboBox()
        spn_box_metric.tmp_lst=[]
        spn_box_metric.tmp_lst.append("*euclidean")
        for lst_itm in spn_box_metric.tmp_lst:
            spn_box_metric.addItem(lst_itm)
        spn_box_metric.currentIndexChanged.connect(self.combobox_changed)

        hbox_metric.addWidget(spn_box_metric)
        bg_box.addLayout(hbox_metric)
        hbox_cutoff =  QHBoxLayout()
        label_cutoff = QLabel("                                cutoff")
        label_cutoff.setFont(QFont("Times",14, QFont.Bold))
        hbox_cutoff.addWidget(label_cutoff)

        spn_box_cutoff = QDoubleSpinBox()
        spn_box_cutoff.local_path = "dummy path"
        spn_box_cutoff.valueChanged.connect(self.spnbox_changed)

        hbox_cutoff.addWidget(spn_box_cutoff)
        bg_box.addLayout(hbox_cutoff)
        hbox_cutoff_criterion =  QHBoxLayout()
        label_cutoff_criterion = QLabel("                                cutoff_criterion")
        label_cutoff_criterion.setFont(QFont("Times",14, QFont.Bold))
        hbox_cutoff_criterion.addWidget(label_cutoff_criterion)

        spn_box_cutoff_criterion = QComboBox()
        spn_box_cutoff_criterion.tmp_lst=[]
        spn_box_cutoff_criterion.tmp_lst.append("*distance")
        spn_box_cutoff_criterion.tmp_lst.append("inconsistent")
        for lst_itm in spn_box_cutoff_criterion.tmp_lst:
            spn_box_cutoff_criterion.addItem(lst_itm)
        spn_box_cutoff_criterion.currentIndexChanged.connect(self.combobox_changed)

        hbox_cutoff_criterion.addWidget(spn_box_cutoff_criterion)
        bg_box.addLayout(hbox_cutoff_criterion)
        label_tst = QLabel("            dbscan")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_eps =  QHBoxLayout()
        label_eps = QLabel("                                eps")
        label_eps.setFont(QFont("Times",14, QFont.Bold))
        hbox_eps.addWidget(label_eps)

        spn_box_eps = QDoubleSpinBox()
        spn_box_eps.local_path = "dummy path"
        spn_box_eps.valueChanged.connect(self.spnbox_changed)

        hbox_eps.addWidget(spn_box_eps)
        bg_box.addLayout(hbox_eps)
        hbox_min_samples =  QHBoxLayout()
        label_min_samples = QLabel("                                min_samples")
        label_min_samples.setFont(QFont("Times",14, QFont.Bold))
        hbox_min_samples.addWidget(label_min_samples)

        spn_box_min_samples = QSpinBox()
        spn_box_min_samples.local_path = "dummy path"
        spn_box_min_samples.valueChanged.connect(self.spnbox_changed)

        hbox_min_samples.addWidget(spn_box_min_samples)
        bg_box.addLayout(hbox_min_samples)
        hbox_min_cluster_size =  QHBoxLayout()
        label_min_cluster_size = QLabel("                        min_cluster_size")
        label_min_cluster_size.setFont(QFont("Times",14, QFont.Bold))
        hbox_min_cluster_size.addWidget(label_min_cluster_size)

        spn_box_min_cluster_size = QSpinBox()
        spn_box_min_cluster_size.local_path = "dummy path"
        spn_box_min_cluster_size.valueChanged.connect(self.spnbox_changed)

        hbox_min_cluster_size.addWidget(spn_box_min_cluster_size)
        bg_box.addLayout(hbox_min_cluster_size)
        hbox_intersection_union_ratio_cutoff =  QHBoxLayout()
        label_intersection_union_ratio_cutoff = QLabel("                        intersection_union_ratio_cutoff")
        label_intersection_union_ratio_cutoff.setFont(QFont("Times",14, QFont.Bold))
        hbox_intersection_union_ratio_cutoff.addWidget(label_intersection_union_ratio_cutoff)

        spn_box_intersection_union_ratio_cutoff = QDoubleSpinBox()
        spn_box_intersection_union_ratio_cutoff.local_path = "dummy path"
        spn_box_intersection_union_ratio_cutoff.valueChanged.connect(self.spnbox_changed)

        hbox_intersection_union_ratio_cutoff.addWidget(spn_box_intersection_union_ratio_cutoff)
        bg_box.addLayout(hbox_intersection_union_ratio_cutoff)
        label_tst = QLabel("    real_space_grid_search")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_characteristic_grid =  QHBoxLayout()
        label_characteristic_grid = QLabel("                characteristic_grid")
        label_characteristic_grid.setFont(QFont("Times",15, QFont.Bold))
        hbox_characteristic_grid.addWidget(label_characteristic_grid)

        spn_box_characteristic_grid = QDoubleSpinBox()
        spn_box_characteristic_grid.local_path = "dummy path"
        spn_box_characteristic_grid.valueChanged.connect(self.spnbox_changed)

        hbox_characteristic_grid.addWidget(spn_box_characteristic_grid)
        bg_box.addLayout(hbox_characteristic_grid)
        label_tst = QLabel("refinement")
        label_tst.setFont(QFont("Monospace", 14, QFont.Bold))
        bg_box.addWidget(label_tst)
        label_tst = QLabel("    mp")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_nproc =  QHBoxLayout()
        label_nproc = QLabel("                nproc")
        label_nproc.setFont(QFont("Times",15, QFont.Bold))
        hbox_nproc.addWidget(label_nproc)

        spn_box_nproc = QSpinBox()
        spn_box_nproc.local_path = "dummy path"
        spn_box_nproc.valueChanged.connect(self.spnbox_changed)

        hbox_nproc.addWidget(spn_box_nproc)
        bg_box.addLayout(hbox_nproc)
        hbox_verbosity =  QHBoxLayout()
        label_verbosity = QLabel("        verbosity")
        label_verbosity.setFont(QFont("Times",16, QFont.Bold))
        hbox_verbosity.addWidget(label_verbosity)

        spn_box_verbosity = QSpinBox()
        spn_box_verbosity.local_path = "dummy path"
        spn_box_verbosity.valueChanged.connect(self.spnbox_changed)

        hbox_verbosity.addWidget(spn_box_verbosity)
        bg_box.addLayout(hbox_verbosity)
        label_tst = QLabel("    parameterisation")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        label_tst = QLabel("        auto_reduction")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_min_nref_per_parameter =  QHBoxLayout()
        label_min_nref_per_parameter = QLabel("                        min_nref_per_parameter")
        label_min_nref_per_parameter.setFont(QFont("Times",14, QFont.Bold))
        hbox_min_nref_per_parameter.addWidget(label_min_nref_per_parameter)

        spn_box_min_nref_per_parameter = QSpinBox()
        spn_box_min_nref_per_parameter.local_path = "dummy path"
        spn_box_min_nref_per_parameter.valueChanged.connect(self.spnbox_changed)

        hbox_min_nref_per_parameter.addWidget(spn_box_min_nref_per_parameter)
        bg_box.addLayout(hbox_min_nref_per_parameter)
        hbox_action =  QHBoxLayout()
        label_action = QLabel("                        action")
        label_action.setFont(QFont("Times",14, QFont.Bold))
        hbox_action.addWidget(label_action)

        spn_box_action = QComboBox()
        spn_box_action.tmp_lst=[]
        spn_box_action.tmp_lst.append("*fail")
        spn_box_action.tmp_lst.append("fix")
        spn_box_action.tmp_lst.append("remove")
        for lst_itm in spn_box_action.tmp_lst:
            spn_box_action.addItem(lst_itm)
        spn_box_action.currentIndexChanged.connect(self.combobox_changed)

        hbox_action.addWidget(spn_box_action)
        bg_box.addLayout(hbox_action)
        label_tst = QLabel("        beam")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_fix =  QHBoxLayout()
        label_fix = QLabel("                        fix")
        label_fix.setFont(QFont("Times",14, QFont.Bold))
        hbox_fix.addWidget(label_fix)

        spn_box_fix = QComboBox()
        spn_box_fix.tmp_lst=[]
        spn_box_fix.tmp_lst.append("all")
        spn_box_fix.tmp_lst.append("*in_spindle_plane")
        spn_box_fix.tmp_lst.append("out_spindle_plane")
        spn_box_fix.tmp_lst.append("*wavelength")
        for lst_itm in spn_box_fix.tmp_lst:
            spn_box_fix.addItem(lst_itm)
        spn_box_fix.currentIndexChanged.connect(self.combobox_changed)

        hbox_fix.addWidget(spn_box_fix)
        bg_box.addLayout(hbox_fix)
        hbox_fix_list =  QHBoxLayout()
        label_fix_list = QLabel("                        fix_list")
        label_fix_list.setFont(QFont("Times",14, QFont.Bold))
        hbox_fix_list.addWidget(label_fix_list)
        label_tst = QLabel("        crystal")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_fix =  QHBoxLayout()
        label_fix = QLabel("                        fix")
        label_fix.setFont(QFont("Times",14, QFont.Bold))
        hbox_fix.addWidget(label_fix)

        spn_box_fix = QComboBox()
        spn_box_fix.tmp_lst=[]
        spn_box_fix.tmp_lst.append("all")
        spn_box_fix.tmp_lst.append("cell")
        spn_box_fix.tmp_lst.append("orientation")
        for lst_itm in spn_box_fix.tmp_lst:
            spn_box_fix.addItem(lst_itm)
        spn_box_fix.currentIndexChanged.connect(self.combobox_changed)

        hbox_fix.addWidget(spn_box_fix)
        bg_box.addLayout(hbox_fix)
        hbox_cell_fix_list =  QHBoxLayout()
        label_cell_fix_list = QLabel("                        cell_fix_list")
        label_cell_fix_list.setFont(QFont("Times",14, QFont.Bold))
        hbox_cell_fix_list.addWidget(label_cell_fix_list)
        hbox_orientation_fix_list =  QHBoxLayout()
        label_orientation_fix_list = QLabel("                        orientation_fix_list")
        label_orientation_fix_list.setFont(QFont("Times",14, QFont.Bold))
        hbox_orientation_fix_list.addWidget(label_orientation_fix_list)
        hbox_scan_varying =  QHBoxLayout()
        label_scan_varying = QLabel("                        scan_varying")
        label_scan_varying.setFont(QFont("Times",14, QFont.Bold))
        hbox_scan_varying.addWidget(label_scan_varying)

        spn_box_scan_varying = QComboBox()
        spn_box_scan_varying.tmp_lst=[]
        spn_box_scan_varying.tmp_lst.append("True")
        spn_box_scan_varying.tmp_lst.append("False")
        for lst_itm in spn_box_scan_varying.tmp_lst:
            spn_box_scan_varying.addItem(lst_itm)
        spn_box_scan_varying.currentIndexChanged.connect(self.combobox_changed)

        hbox_scan_varying.addWidget(spn_box_scan_varying)
        bg_box.addLayout(hbox_scan_varying)
        hbox_num_intervals =  QHBoxLayout()
        label_num_intervals = QLabel("                        num_intervals")
        label_num_intervals.setFont(QFont("Times",14, QFont.Bold))
        hbox_num_intervals.addWidget(label_num_intervals)

        spn_box_num_intervals = QComboBox()
        spn_box_num_intervals.tmp_lst=[]
        spn_box_num_intervals.tmp_lst.append("*fixed_width")
        spn_box_num_intervals.tmp_lst.append("absolute")
        for lst_itm in spn_box_num_intervals.tmp_lst:
            spn_box_num_intervals.addItem(lst_itm)
        spn_box_num_intervals.currentIndexChanged.connect(self.combobox_changed)

        hbox_num_intervals.addWidget(spn_box_num_intervals)
        bg_box.addLayout(hbox_num_intervals)
        hbox_interval_width_degrees =  QHBoxLayout()
        label_interval_width_degrees = QLabel("                        interval_width_degrees")
        label_interval_width_degrees.setFont(QFont("Times",14, QFont.Bold))
        hbox_interval_width_degrees.addWidget(label_interval_width_degrees)

        spn_box_interval_width_degrees = QDoubleSpinBox()
        spn_box_interval_width_degrees.local_path = "dummy path"
        spn_box_interval_width_degrees.valueChanged.connect(self.spnbox_changed)

        hbox_interval_width_degrees.addWidget(spn_box_interval_width_degrees)
        bg_box.addLayout(hbox_interval_width_degrees)
        hbox_absolute_num_intervals =  QHBoxLayout()
        label_absolute_num_intervals = QLabel("                        absolute_num_intervals")
        label_absolute_num_intervals.setFont(QFont("Times",14, QFont.Bold))
        hbox_absolute_num_intervals.addWidget(label_absolute_num_intervals)

        spn_box_absolute_num_intervals = QSpinBox()
        spn_box_absolute_num_intervals.local_path = "dummy path"
        spn_box_absolute_num_intervals.valueChanged.connect(self.spnbox_changed)

        hbox_absolute_num_intervals.addWidget(spn_box_absolute_num_intervals)
        bg_box.addLayout(hbox_absolute_num_intervals)
        hbox_UB_model_per =  QHBoxLayout()
        label_UB_model_per = QLabel("                        UB_model_per")
        label_UB_model_per.setFont(QFont("Times",14, QFont.Bold))
        hbox_UB_model_per.addWidget(label_UB_model_per)

        spn_box_UB_model_per = QComboBox()
        spn_box_UB_model_per.tmp_lst=[]
        spn_box_UB_model_per.tmp_lst.append("reflection")
        spn_box_UB_model_per.tmp_lst.append("image")
        spn_box_UB_model_per.tmp_lst.append("*block")
        for lst_itm in spn_box_UB_model_per.tmp_lst:
            spn_box_UB_model_per.addItem(lst_itm)
        spn_box_UB_model_per.currentIndexChanged.connect(self.combobox_changed)

        hbox_UB_model_per.addWidget(spn_box_UB_model_per)
        bg_box.addLayout(hbox_UB_model_per)
        label_tst = QLabel("        detector")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_panels =  QHBoxLayout()
        label_panels = QLabel("                        panels")
        label_panels.setFont(QFont("Times",14, QFont.Bold))
        hbox_panels.addWidget(label_panels)

        spn_box_panels = QComboBox()
        spn_box_panels.tmp_lst=[]
        spn_box_panels.tmp_lst.append("*automatic")
        spn_box_panels.tmp_lst.append("single")
        spn_box_panels.tmp_lst.append("multiple")
        spn_box_panels.tmp_lst.append("hierarchical")
        for lst_itm in spn_box_panels.tmp_lst:
            spn_box_panels.addItem(lst_itm)
        spn_box_panels.currentIndexChanged.connect(self.combobox_changed)

        hbox_panels.addWidget(spn_box_panels)
        bg_box.addLayout(hbox_panels)
        hbox_hierarchy_level =  QHBoxLayout()
        label_hierarchy_level = QLabel("                        hierarchy_level")
        label_hierarchy_level.setFont(QFont("Times",14, QFont.Bold))
        hbox_hierarchy_level.addWidget(label_hierarchy_level)

        spn_box_hierarchy_level = QSpinBox()
        spn_box_hierarchy_level.local_path = "dummy path"
        spn_box_hierarchy_level.valueChanged.connect(self.spnbox_changed)

        hbox_hierarchy_level.addWidget(spn_box_hierarchy_level)
        bg_box.addLayout(hbox_hierarchy_level)
        hbox_fix =  QHBoxLayout()
        label_fix = QLabel("                        fix")
        label_fix.setFont(QFont("Times",14, QFont.Bold))
        hbox_fix.addWidget(label_fix)

        spn_box_fix = QComboBox()
        spn_box_fix.tmp_lst=[]
        spn_box_fix.tmp_lst.append("all")
        spn_box_fix.tmp_lst.append("position")
        spn_box_fix.tmp_lst.append("orientation")
        for lst_itm in spn_box_fix.tmp_lst:
            spn_box_fix.addItem(lst_itm)
        spn_box_fix.currentIndexChanged.connect(self.combobox_changed)

        hbox_fix.addWidget(spn_box_fix)
        bg_box.addLayout(hbox_fix)
        hbox_fix_list =  QHBoxLayout()
        label_fix_list = QLabel("                        fix_list")
        label_fix_list.setFont(QFont("Times",14, QFont.Bold))
        hbox_fix_list.addWidget(label_fix_list)
        hbox_sparse =  QHBoxLayout()
        label_sparse = QLabel("                sparse")
        label_sparse.setFont(QFont("Times",15, QFont.Bold))
        hbox_sparse.addWidget(label_sparse)

        spn_box_sparse = QComboBox()
        spn_box_sparse.tmp_lst=[]
        spn_box_sparse.tmp_lst.append("True")
        spn_box_sparse.tmp_lst.append("False")
        for lst_itm in spn_box_sparse.tmp_lst:
            spn_box_sparse.addItem(lst_itm)
        spn_box_sparse.currentIndexChanged.connect(self.combobox_changed)

        hbox_sparse.addWidget(spn_box_sparse)
        bg_box.addLayout(hbox_sparse)
        hbox_treat_single_image_as_still =  QHBoxLayout()
        label_treat_single_image_as_still = QLabel("                treat_single_image_as_still")
        label_treat_single_image_as_still.setFont(QFont("Times",15, QFont.Bold))
        hbox_treat_single_image_as_still.addWidget(label_treat_single_image_as_still)

        spn_box_treat_single_image_as_still = QComboBox()
        spn_box_treat_single_image_as_still.tmp_lst=[]
        spn_box_treat_single_image_as_still.tmp_lst.append("True")
        spn_box_treat_single_image_as_still.tmp_lst.append("False")
        for lst_itm in spn_box_treat_single_image_as_still.tmp_lst:
            spn_box_treat_single_image_as_still.addItem(lst_itm)
        spn_box_treat_single_image_as_still.currentIndexChanged.connect(self.combobox_changed)

        hbox_treat_single_image_as_still.addWidget(spn_box_treat_single_image_as_still)
        bg_box.addLayout(hbox_treat_single_image_as_still)
        label_tst = QLabel("    refinery")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_engine =  QHBoxLayout()
        label_engine = QLabel("                engine")
        label_engine.setFont(QFont("Times",15, QFont.Bold))
        hbox_engine.addWidget(label_engine)

        spn_box_engine = QComboBox()
        spn_box_engine.tmp_lst=[]
        spn_box_engine.tmp_lst.append("SimpleLBFGS")
        spn_box_engine.tmp_lst.append("LBFGScurvs")
        spn_box_engine.tmp_lst.append("GaussNewton")
        spn_box_engine.tmp_lst.append("*LevMar")
        for lst_itm in spn_box_engine.tmp_lst:
            spn_box_engine.addItem(lst_itm)
        spn_box_engine.currentIndexChanged.connect(self.combobox_changed)

        hbox_engine.addWidget(spn_box_engine)
        bg_box.addLayout(hbox_engine)
        hbox_track_step =  QHBoxLayout()
        label_track_step = QLabel("                track_step")
        label_track_step.setFont(QFont("Times",15, QFont.Bold))
        hbox_track_step.addWidget(label_track_step)

        spn_box_track_step = QComboBox()
        spn_box_track_step.tmp_lst=[]
        spn_box_track_step.tmp_lst.append("True")
        spn_box_track_step.tmp_lst.append("False")
        for lst_itm in spn_box_track_step.tmp_lst:
            spn_box_track_step.addItem(lst_itm)
        spn_box_track_step.currentIndexChanged.connect(self.combobox_changed)

        hbox_track_step.addWidget(spn_box_track_step)
        bg_box.addLayout(hbox_track_step)
        hbox_track_gradient =  QHBoxLayout()
        label_track_gradient = QLabel("                track_gradient")
        label_track_gradient.setFont(QFont("Times",15, QFont.Bold))
        hbox_track_gradient.addWidget(label_track_gradient)

        spn_box_track_gradient = QComboBox()
        spn_box_track_gradient.tmp_lst=[]
        spn_box_track_gradient.tmp_lst.append("True")
        spn_box_track_gradient.tmp_lst.append("False")
        for lst_itm in spn_box_track_gradient.tmp_lst:
            spn_box_track_gradient.addItem(lst_itm)
        spn_box_track_gradient.currentIndexChanged.connect(self.combobox_changed)

        hbox_track_gradient.addWidget(spn_box_track_gradient)
        bg_box.addLayout(hbox_track_gradient)
        hbox_track_parameter_correlation =  QHBoxLayout()
        label_track_parameter_correlation = QLabel("                track_parameter_correlation")
        label_track_parameter_correlation.setFont(QFont("Times",15, QFont.Bold))
        hbox_track_parameter_correlation.addWidget(label_track_parameter_correlation)

        spn_box_track_parameter_correlation = QComboBox()
        spn_box_track_parameter_correlation.tmp_lst=[]
        spn_box_track_parameter_correlation.tmp_lst.append("True")
        spn_box_track_parameter_correlation.tmp_lst.append("False")
        for lst_itm in spn_box_track_parameter_correlation.tmp_lst:
            spn_box_track_parameter_correlation.addItem(lst_itm)
        spn_box_track_parameter_correlation.currentIndexChanged.connect(self.combobox_changed)

        hbox_track_parameter_correlation.addWidget(spn_box_track_parameter_correlation)
        bg_box.addLayout(hbox_track_parameter_correlation)
        hbox_track_out_of_sample_rmsd =  QHBoxLayout()
        label_track_out_of_sample_rmsd = QLabel("                track_out_of_sample_rmsd")
        label_track_out_of_sample_rmsd.setFont(QFont("Times",15, QFont.Bold))
        hbox_track_out_of_sample_rmsd.addWidget(label_track_out_of_sample_rmsd)

        spn_box_track_out_of_sample_rmsd = QComboBox()
        spn_box_track_out_of_sample_rmsd.tmp_lst=[]
        spn_box_track_out_of_sample_rmsd.tmp_lst.append("True")
        spn_box_track_out_of_sample_rmsd.tmp_lst.append("False")
        for lst_itm in spn_box_track_out_of_sample_rmsd.tmp_lst:
            spn_box_track_out_of_sample_rmsd.addItem(lst_itm)
        spn_box_track_out_of_sample_rmsd.currentIndexChanged.connect(self.combobox_changed)

        hbox_track_out_of_sample_rmsd.addWidget(spn_box_track_out_of_sample_rmsd)
        bg_box.addLayout(hbox_track_out_of_sample_rmsd)
        hbox_log =  QHBoxLayout()
        label_log = QLabel("                log")
        label_log.setFont(QFont("Times",15, QFont.Bold))
        hbox_log.addWidget(label_log)
        hbox_max_iterations =  QHBoxLayout()
        label_max_iterations = QLabel("                max_iterations")
        label_max_iterations.setFont(QFont("Times",15, QFont.Bold))
        hbox_max_iterations.addWidget(label_max_iterations)

        spn_box_max_iterations = QSpinBox()
        spn_box_max_iterations.local_path = "dummy path"
        spn_box_max_iterations.valueChanged.connect(self.spnbox_changed)

        hbox_max_iterations.addWidget(spn_box_max_iterations)
        bg_box.addLayout(hbox_max_iterations)
        label_tst = QLabel("    target")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_rmsd_cutoff =  QHBoxLayout()
        label_rmsd_cutoff = QLabel("                rmsd_cutoff")
        label_rmsd_cutoff.setFont(QFont("Times",15, QFont.Bold))
        hbox_rmsd_cutoff.addWidget(label_rmsd_cutoff)

        spn_box_rmsd_cutoff = QComboBox()
        spn_box_rmsd_cutoff.tmp_lst=[]
        spn_box_rmsd_cutoff.tmp_lst.append("*fraction_of_bin_size")
        spn_box_rmsd_cutoff.tmp_lst.append("absolute")
        for lst_itm in spn_box_rmsd_cutoff.tmp_lst:
            spn_box_rmsd_cutoff.addItem(lst_itm)
        spn_box_rmsd_cutoff.currentIndexChanged.connect(self.combobox_changed)

        hbox_rmsd_cutoff.addWidget(spn_box_rmsd_cutoff)
        bg_box.addLayout(hbox_rmsd_cutoff)
        hbox_bin_size_fraction =  QHBoxLayout()
        label_bin_size_fraction = QLabel("                bin_size_fraction")
        label_bin_size_fraction.setFont(QFont("Times",15, QFont.Bold))
        hbox_bin_size_fraction.addWidget(label_bin_size_fraction)

        spn_box_bin_size_fraction = QDoubleSpinBox()
        spn_box_bin_size_fraction.local_path = "dummy path"
        spn_box_bin_size_fraction.valueChanged.connect(self.spnbox_changed)

        hbox_bin_size_fraction.addWidget(spn_box_bin_size_fraction)
        bg_box.addLayout(hbox_bin_size_fraction)
        hbox_absolute_cutoffs =  QHBoxLayout()
        label_absolute_cutoffs = QLabel("                absolute_cutoffs")
        label_absolute_cutoffs.setFont(QFont("Times",15, QFont.Bold))
        hbox_absolute_cutoffs.addWidget(label_absolute_cutoffs)
        hbox_gradient_calculation_blocksize =  QHBoxLayout()
        label_gradient_calculation_blocksize = QLabel("                gradient_calculation_blocksize")
        label_gradient_calculation_blocksize.setFont(QFont("Times",15, QFont.Bold))
        hbox_gradient_calculation_blocksize.addWidget(label_gradient_calculation_blocksize)

        spn_box_gradient_calculation_blocksize = QSpinBox()
        spn_box_gradient_calculation_blocksize.local_path = "dummy path"
        spn_box_gradient_calculation_blocksize.valueChanged.connect(self.spnbox_changed)

        hbox_gradient_calculation_blocksize.addWidget(spn_box_gradient_calculation_blocksize)
        bg_box.addLayout(hbox_gradient_calculation_blocksize)
        label_tst = QLabel("    reflections")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_reflections_per_degree =  QHBoxLayout()
        label_reflections_per_degree = QLabel("                reflections_per_degree")
        label_reflections_per_degree.setFont(QFont("Times",15, QFont.Bold))
        hbox_reflections_per_degree.addWidget(label_reflections_per_degree)

        spn_box_reflections_per_degree = QDoubleSpinBox()
        spn_box_reflections_per_degree.local_path = "dummy path"
        spn_box_reflections_per_degree.valueChanged.connect(self.spnbox_changed)

        hbox_reflections_per_degree.addWidget(spn_box_reflections_per_degree)
        bg_box.addLayout(hbox_reflections_per_degree)
        hbox_minimum_sample_size =  QHBoxLayout()
        label_minimum_sample_size = QLabel("                minimum_sample_size")
        label_minimum_sample_size.setFont(QFont("Times",15, QFont.Bold))
        hbox_minimum_sample_size.addWidget(label_minimum_sample_size)

        spn_box_minimum_sample_size = QSpinBox()
        spn_box_minimum_sample_size.local_path = "dummy path"
        spn_box_minimum_sample_size.valueChanged.connect(self.spnbox_changed)

        hbox_minimum_sample_size.addWidget(spn_box_minimum_sample_size)
        bg_box.addLayout(hbox_minimum_sample_size)
        hbox_maximum_sample_size =  QHBoxLayout()
        label_maximum_sample_size = QLabel("                maximum_sample_size")
        label_maximum_sample_size.setFont(QFont("Times",15, QFont.Bold))
        hbox_maximum_sample_size.addWidget(label_maximum_sample_size)

        spn_box_maximum_sample_size = QSpinBox()
        spn_box_maximum_sample_size.local_path = "dummy path"
        spn_box_maximum_sample_size.valueChanged.connect(self.spnbox_changed)

        hbox_maximum_sample_size.addWidget(spn_box_maximum_sample_size)
        bg_box.addLayout(hbox_maximum_sample_size)
        hbox_use_all_reflections =  QHBoxLayout()
        label_use_all_reflections = QLabel("                use_all_reflections")
        label_use_all_reflections.setFont(QFont("Times",15, QFont.Bold))
        hbox_use_all_reflections.addWidget(label_use_all_reflections)

        spn_box_use_all_reflections = QComboBox()
        spn_box_use_all_reflections.tmp_lst=[]
        spn_box_use_all_reflections.tmp_lst.append("True")
        spn_box_use_all_reflections.tmp_lst.append("False")
        for lst_itm in spn_box_use_all_reflections.tmp_lst:
            spn_box_use_all_reflections.addItem(lst_itm)
        spn_box_use_all_reflections.currentIndexChanged.connect(self.combobox_changed)

        hbox_use_all_reflections.addWidget(spn_box_use_all_reflections)
        bg_box.addLayout(hbox_use_all_reflections)
        hbox_random_seed =  QHBoxLayout()
        label_random_seed = QLabel("                random_seed")
        label_random_seed.setFont(QFont("Times",15, QFont.Bold))
        hbox_random_seed.addWidget(label_random_seed)

        spn_box_random_seed = QSpinBox()
        spn_box_random_seed.local_path = "dummy path"
        spn_box_random_seed.valueChanged.connect(self.spnbox_changed)

        hbox_random_seed.addWidget(spn_box_random_seed)
        bg_box.addLayout(hbox_random_seed)
        hbox_close_to_spindle_cutoff =  QHBoxLayout()
        label_close_to_spindle_cutoff = QLabel("                close_to_spindle_cutoff")
        label_close_to_spindle_cutoff.setFont(QFont("Times",15, QFont.Bold))
        hbox_close_to_spindle_cutoff.addWidget(label_close_to_spindle_cutoff)

        spn_box_close_to_spindle_cutoff = QDoubleSpinBox()
        spn_box_close_to_spindle_cutoff.local_path = "dummy path"
        spn_box_close_to_spindle_cutoff.valueChanged.connect(self.spnbox_changed)

        hbox_close_to_spindle_cutoff.addWidget(spn_box_close_to_spindle_cutoff)
        bg_box.addLayout(hbox_close_to_spindle_cutoff)
        hbox_block_width =  QHBoxLayout()
        label_block_width = QLabel("                block_width")
        label_block_width.setFont(QFont("Times",15, QFont.Bold))
        hbox_block_width.addWidget(label_block_width)

        spn_box_block_width = QDoubleSpinBox()
        spn_box_block_width.local_path = "dummy path"
        spn_box_block_width.valueChanged.connect(self.spnbox_changed)

        hbox_block_width.addWidget(spn_box_block_width)
        bg_box.addLayout(hbox_block_width)
        label_tst = QLabel("        weighting_strategy")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_override =  QHBoxLayout()
        label_override = QLabel("                        override")
        label_override.setFont(QFont("Times",14, QFont.Bold))
        hbox_override.addWidget(label_override)

        spn_box_override = QComboBox()
        spn_box_override.tmp_lst=[]
        spn_box_override.tmp_lst.append("statistical")
        spn_box_override.tmp_lst.append("stills")
        spn_box_override.tmp_lst.append("constant")
        for lst_itm in spn_box_override.tmp_lst:
            spn_box_override.addItem(lst_itm)
        spn_box_override.currentIndexChanged.connect(self.combobox_changed)

        hbox_override.addWidget(spn_box_override)
        bg_box.addLayout(hbox_override)
        hbox_delpsi_constant =  QHBoxLayout()
        label_delpsi_constant = QLabel("                        delpsi_constant")
        label_delpsi_constant.setFont(QFont("Times",14, QFont.Bold))
        hbox_delpsi_constant.addWidget(label_delpsi_constant)

        spn_box_delpsi_constant = QDoubleSpinBox()
        spn_box_delpsi_constant.local_path = "dummy path"
        spn_box_delpsi_constant.valueChanged.connect(self.spnbox_changed)

        hbox_delpsi_constant.addWidget(spn_box_delpsi_constant)
        bg_box.addLayout(hbox_delpsi_constant)
        hbox_constants =  QHBoxLayout()
        label_constants = QLabel("                        constants")
        label_constants.setFont(QFont("Times",14, QFont.Bold))
        hbox_constants.addWidget(label_constants)
        label_tst = QLabel("        outlier")
        label_tst.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_algorithm =  QHBoxLayout()
        label_algorithm = QLabel("                        algorithm")
        label_algorithm.setFont(QFont("Times",14, QFont.Bold))
        hbox_algorithm.addWidget(label_algorithm)

        spn_box_algorithm = QComboBox()
        spn_box_algorithm.tmp_lst=[]
        spn_box_algorithm.tmp_lst.append("null")
        spn_box_algorithm.tmp_lst.append("*auto")
        spn_box_algorithm.tmp_lst.append("mcd")
        spn_box_algorithm.tmp_lst.append("tukey")
        spn_box_algorithm.tmp_lst.append("sauter_poon")
        for lst_itm in spn_box_algorithm.tmp_lst:
            spn_box_algorithm.addItem(lst_itm)
        spn_box_algorithm.currentIndexChanged.connect(self.combobox_changed)

        hbox_algorithm.addWidget(spn_box_algorithm)
        bg_box.addLayout(hbox_algorithm)
        hbox_minimum_number_of_reflections =  QHBoxLayout()
        label_minimum_number_of_reflections = QLabel("                        minimum_number_of_reflections")
        label_minimum_number_of_reflections.setFont(QFont("Times",14, QFont.Bold))
        hbox_minimum_number_of_reflections.addWidget(label_minimum_number_of_reflections)

        spn_box_minimum_number_of_reflections = QSpinBox()
        spn_box_minimum_number_of_reflections.local_path = "dummy path"
        spn_box_minimum_number_of_reflections.valueChanged.connect(self.spnbox_changed)

        hbox_minimum_number_of_reflections.addWidget(spn_box_minimum_number_of_reflections)
        bg_box.addLayout(hbox_minimum_number_of_reflections)
        hbox_separate_experiments =  QHBoxLayout()
        label_separate_experiments = QLabel("                        separate_experiments")
        label_separate_experiments.setFont(QFont("Times",14, QFont.Bold))
        hbox_separate_experiments.addWidget(label_separate_experiments)

        spn_box_separate_experiments = QComboBox()
        spn_box_separate_experiments.tmp_lst=[]
        spn_box_separate_experiments.tmp_lst.append("True")
        spn_box_separate_experiments.tmp_lst.append("False")
        for lst_itm in spn_box_separate_experiments.tmp_lst:
            spn_box_separate_experiments.addItem(lst_itm)
        spn_box_separate_experiments.currentIndexChanged.connect(self.combobox_changed)

        hbox_separate_experiments.addWidget(spn_box_separate_experiments)
        bg_box.addLayout(hbox_separate_experiments)
        hbox_separate_panels =  QHBoxLayout()
        label_separate_panels = QLabel("                        separate_panels")
        label_separate_panels.setFont(QFont("Times",14, QFont.Bold))
        hbox_separate_panels.addWidget(label_separate_panels)

        spn_box_separate_panels = QComboBox()
        spn_box_separate_panels.tmp_lst=[]
        spn_box_separate_panels.tmp_lst.append("True")
        spn_box_separate_panels.tmp_lst.append("False")
        for lst_itm in spn_box_separate_panels.tmp_lst:
            spn_box_separate_panels.addItem(lst_itm)
        spn_box_separate_panels.currentIndexChanged.connect(self.combobox_changed)

        hbox_separate_panels.addWidget(spn_box_separate_panels)
        bg_box.addLayout(hbox_separate_panels)
        label_tst = QLabel("            tukey")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_iqr_multiplier =  QHBoxLayout()
        label_iqr_multiplier = QLabel("                                iqr_multiplier")
        label_iqr_multiplier.setFont(QFont("Times",14, QFont.Bold))
        hbox_iqr_multiplier.addWidget(label_iqr_multiplier)

        spn_box_iqr_multiplier = QDoubleSpinBox()
        spn_box_iqr_multiplier.local_path = "dummy path"
        spn_box_iqr_multiplier.valueChanged.connect(self.spnbox_changed)

        hbox_iqr_multiplier.addWidget(spn_box_iqr_multiplier)
        bg_box.addLayout(hbox_iqr_multiplier)
        label_tst = QLabel("            mcd")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_alpha =  QHBoxLayout()
        label_alpha = QLabel("                                alpha")
        label_alpha.setFont(QFont("Times",14, QFont.Bold))
        hbox_alpha.addWidget(label_alpha)

        spn_box_alpha = QDoubleSpinBox()
        spn_box_alpha.local_path = "dummy path"
        spn_box_alpha.valueChanged.connect(self.spnbox_changed)

        hbox_alpha.addWidget(spn_box_alpha)
        bg_box.addLayout(hbox_alpha)
        hbox_max_n_groups =  QHBoxLayout()
        label_max_n_groups = QLabel("                                max_n_groups")
        label_max_n_groups.setFont(QFont("Times",14, QFont.Bold))
        hbox_max_n_groups.addWidget(label_max_n_groups)

        spn_box_max_n_groups = QSpinBox()
        spn_box_max_n_groups.local_path = "dummy path"
        spn_box_max_n_groups.valueChanged.connect(self.spnbox_changed)

        hbox_max_n_groups.addWidget(spn_box_max_n_groups)
        bg_box.addLayout(hbox_max_n_groups)
        hbox_min_group_size =  QHBoxLayout()
        label_min_group_size = QLabel("                                min_group_size")
        label_min_group_size.setFont(QFont("Times",14, QFont.Bold))
        hbox_min_group_size.addWidget(label_min_group_size)

        spn_box_min_group_size = QSpinBox()
        spn_box_min_group_size.local_path = "dummy path"
        spn_box_min_group_size.valueChanged.connect(self.spnbox_changed)

        hbox_min_group_size.addWidget(spn_box_min_group_size)
        bg_box.addLayout(hbox_min_group_size)
        hbox_n_trials =  QHBoxLayout()
        label_n_trials = QLabel("                                n_trials")
        label_n_trials.setFont(QFont("Times",14, QFont.Bold))
        hbox_n_trials.addWidget(label_n_trials)

        spn_box_n_trials = QSpinBox()
        spn_box_n_trials.local_path = "dummy path"
        spn_box_n_trials.valueChanged.connect(self.spnbox_changed)

        hbox_n_trials.addWidget(spn_box_n_trials)
        bg_box.addLayout(hbox_n_trials)
        hbox_k1 =  QHBoxLayout()
        label_k1 = QLabel("                                k1")
        label_k1.setFont(QFont("Times",14, QFont.Bold))
        hbox_k1.addWidget(label_k1)

        spn_box_k1 = QSpinBox()
        spn_box_k1.local_path = "dummy path"
        spn_box_k1.valueChanged.connect(self.spnbox_changed)

        hbox_k1.addWidget(spn_box_k1)
        bg_box.addLayout(hbox_k1)
        hbox_k2 =  QHBoxLayout()
        label_k2 = QLabel("                                k2")
        label_k2.setFont(QFont("Times",14, QFont.Bold))
        hbox_k2.addWidget(label_k2)

        spn_box_k2 = QSpinBox()
        spn_box_k2.local_path = "dummy path"
        spn_box_k2.valueChanged.connect(self.spnbox_changed)

        hbox_k2.addWidget(spn_box_k2)
        bg_box.addLayout(hbox_k2)
        hbox_k3 =  QHBoxLayout()
        label_k3 = QLabel("                                k3")
        label_k3.setFont(QFont("Times",14, QFont.Bold))
        hbox_k3.addWidget(label_k3)

        spn_box_k3 = QSpinBox()
        spn_box_k3.local_path = "dummy path"
        spn_box_k3.valueChanged.connect(self.spnbox_changed)

        hbox_k3.addWidget(spn_box_k3)
        bg_box.addLayout(hbox_k3)
        hbox_threshold_probability =  QHBoxLayout()
        label_threshold_probability = QLabel("                                threshold_probability")
        label_threshold_probability.setFont(QFont("Times",14, QFont.Bold))
        hbox_threshold_probability.addWidget(label_threshold_probability)

        spn_box_threshold_probability = QDoubleSpinBox()
        spn_box_threshold_probability.local_path = "dummy path"
        spn_box_threshold_probability.valueChanged.connect(self.spnbox_changed)

        hbox_threshold_probability.addWidget(spn_box_threshold_probability)
        bg_box.addLayout(hbox_threshold_probability)
        label_tst = QLabel("            sauter_poon")
        label_tst.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_px_sz =  QHBoxLayout()
        label_px_sz = QLabel("                                px_sz")
        label_px_sz.setFont(QFont("Times",14, QFont.Bold))
        hbox_px_sz.addWidget(label_px_sz)
        hbox_verbose =  QHBoxLayout()
        label_verbose = QLabel("                                verbose")
        label_verbose.setFont(QFont("Times",14, QFont.Bold))
        hbox_verbose.addWidget(label_verbose)

        spn_box_verbose = QComboBox()
        spn_box_verbose.tmp_lst=[]
        spn_box_verbose.tmp_lst.append("True")
        spn_box_verbose.tmp_lst.append("False")
        for lst_itm in spn_box_verbose.tmp_lst:
            spn_box_verbose.addItem(lst_itm)
        spn_box_verbose.currentIndexChanged.connect(self.combobox_changed)

        hbox_verbose.addWidget(spn_box_verbose)
        bg_box.addLayout(hbox_verbose)
        hbox_pdf =  QHBoxLayout()
        label_pdf = QLabel("                                pdf")
        label_pdf.setFont(QFont("Times",14, QFont.Bold))
        hbox_pdf.addWidget(label_pdf)

        spn_box_pdf = QLineEdit()
        spn_box_pdf.local_path = "dummy path"
        spn_box_pdf.textChanged.connect(self.spnbox_changed)

        hbox_pdf.addWidget(spn_box_pdf)
        bg_box.addLayout(hbox_pdf)
        label_tst = QLabel("output")
        label_tst.setFont(QFont("Monospace", 14, QFont.Bold))
        bg_box.addWidget(label_tst)
        hbox_experiments =  QHBoxLayout()
        label_experiments = QLabel("        experiments")
        label_experiments.setFont(QFont("Times",16, QFont.Bold))
        hbox_experiments.addWidget(label_experiments)
        hbox_reflections =  QHBoxLayout()
        label_reflections = QLabel("        reflections")
        label_reflections.setFont(QFont("Times",16, QFont.Bold))
        hbox_reflections.addWidget(label_reflections)
        hbox_unindexed_reflections =  QHBoxLayout()
        label_unindexed_reflections = QLabel("        unindexed_reflections")
        label_unindexed_reflections.setFont(QFont("Times",16, QFont.Bold))
        hbox_unindexed_reflections.addWidget(label_unindexed_reflections)
        hbox_verbosity =  QHBoxLayout()
        label_verbosity = QLabel("verbosity")
        label_verbosity.setFont(QFont("Times",18, QFont.Bold))
        hbox_verbosity.addWidget(label_verbosity)

        spn_box_verbosity = QSpinBox()
        spn_box_verbosity.local_path = "dummy path"
        spn_box_verbosity.valueChanged.connect(self.spnbox_changed)

        hbox_verbosity.addWidget(spn_box_verbosity)
        bg_box.addLayout(hbox_verbosity)
 
        self.setLayout(bg_box)
        self.show()


    def spnbox_changed(self, value):
        sender = self.sender()
        print "sender =", sender
        print "spnbox_changed to:", value


    def combobox_changed(self, value):
        sender = self.sender()
        print "sender =", sender
        print "combobox_changed to:"
        print sender.tmp_lst[value] 


class ParamMainWidget( QWidget):
    def __init__(self):
        super(ParamMainWidget, self).__init__()
        self.scrollable_widget = inner_widg(self)
        scrollArea = QScrollArea()
        scrollArea.setWidget(self.scrollable_widget)
        hbox =  QHBoxLayout()
        hbox.addWidget(scrollArea)
        self.setLayout(hbox)
        self.setWindowTitle('Phil dialog')
        self.show()


    def to_be_caled_from_son_widg(self):
        print "from parent parent_widget"


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = ParamMainWidget()
    sys.exit(app.exec_())

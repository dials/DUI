import sys

def write_script(self_path):

    print "writing setpath.sh"
    print

    lst_lin = []
    lst_lin.append( "# autogenerated setpath script\n")
    lst_lin.append( "# do not modify this script, run setup_setpath.sh instead\n")
    lst_lin.append( " \n")
    lst_lin.append( "echo \"This script should be run with the source command\"\n")
    lst_lin.append( "echo \"setting up tmp path\"\n")

    lst_lin.append( "MY_WORKING_DIR=$(pwd)\n")


    line_w_path = "export DUI_PATH=\""
    line_w_path += self_path
    line_w_path += "\"\n"
    lst_lin.append( line_w_path)

    lst_lin.append( "export PATH=$PATH:$DUI_PATH\n")
    lst_lin.append( "cd $DUI_PATH\n")
    lst_lin.append( "echo \"DUI_PATH =$DUI_PATH\"\n")
    lst_lin.append( "cd ../idials_GUI/\n")
    lst_lin.append( "export IDIALS_GUI_PATH=$(pwd)\n")
    lst_lin.append( "echo \"IDIALS_GUI_PATH=$IDIALS_GUI_PATH\"\n")
    lst_lin.append( "echo \"done\"\n")

    lst_lin.append( "cd $MY_WORKING_DIR\n")


    lst_lin.append( "echo \" \"\n")

    line_x_tut = "echo \"type "
    line_x_tut = line_x_tut + "\\" + "\"" + "dui_idials" + "\\" + "\""
    line_x_tut = line_x_tut + " (without quotes) to launch DUI/iDIALS\" \n"
    lst_lin.append(line_x_tut)

    lst_lin.append( "echo \" \"\n")
    lst_lin.append( " \n")

    myfile = open("setpath.sh", "w")

    for line in lst_lin:
        myfile.write(line)

    myfile.close()


if( __name__ == "__main__" ):

    if( len(sys.argv) > 1 ):
        self_path = sys.argv[1]
        write_script(self_path)
    else:
        print "no path to connect provided"

    print "setpath.sh generated with the path: ", self_path
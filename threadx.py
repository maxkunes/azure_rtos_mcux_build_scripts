import os
import shutil

# get list of all source files in threadx-master/common/src/
src_files = os.listdir('threadx-master\\common\\src\\')
# get list of all header files in threadx-master/common/inc/
header_files = os.listdir('threadx-master\\common\\inc\\')
# get list of asm files in threadx-master/ports/cortex_m7/gnu/src
asm_files = os.listdir('threadx-master\\ports\\cortex_m7\\gnu\\src\\')


def try_remove_folder(path):
    try:
        shutil.rmtree(path)
    except:
        pass


def try_remove_file(path):
    try:
        os.remove(path)
    except:
        pass


try_remove_folder('generated\\threadx\\src')
try_remove_folder('generated\\threadx\\include')
try_remove_folder('generated\\threadx\\asm')
try_remove_file('generated\\threadx\\threadx.c')

os.makedirs('generated\\threadx\\src', exist_ok=True)
os.makedirs('generated\\threadx\\include', exist_ok=True)
os.makedirs('generated\\threadx\\asm', exist_ok=True)

# generate master c file to compile all other c files
# and copy over files
with open('generated\\threadx\\threadx.c', 'w') as master_file:
    for src in src_files:

        # copy source file to output directory
        shutil.copy('threadx-master\\common\\src\\{}'.format(src),
                    'generated\\threadx\\src')

        # write include line in master_file
        master_file.write('#include "src/{}"\n'.format(src))

# copy over header files
for header in header_files:
    # copy source file to output directory
    shutil.copy('threadx-master\\common\\inc\\{}'.format(header),
                'generated\\threadx\\include')

# copy cortex_m7 gnu header to includes
shutil.copy('threadx-master\\ports\\cortex_m7\\gnu\\inc\\tx_port.h',
            'generated\\threadx\\include')

# copy over asm files
for asm in asm_files:
    # copy source file to output directory
    shutil.copy('threadx-master\\ports\\cortex_m7\\gnu\\src\\{}'.format(asm),
                'generated\\threadx\\asm')

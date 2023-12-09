import os
import sys
import subprocess

def run_command(command, ofile):
  print(f"Command:\n{command}\n", file=ofile)
  print(subprocess.check_output(command, shell=True).decode("utf-8"), file=ofile)

def main():
  os.chdir(os.path.dirname(os.path.abspath(__file__)))
  artifacts_dir = '../artifacts'

  ofile = open(f'{artifacts_dir}/01-nl.txt', 'w')
  run_command("printf 'aboba\nboba\n' | python3 01-nl.py", ofile)
  run_command("python3 01-nl.py 01-nl.py", ofile)
  ofile.close()

  ofile = open(f'{artifacts_dir}/02-tail.txt', 'w')
  run_command("printf 'a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n' | python3 02-tail.py", ofile)
  run_command("python3 02-tail.py 02-tail.py", ofile)
  run_command("python3 02-tail.py 02-tail.py 02-tail.py", ofile)
  ofile.close()

  ofile = open(f'{artifacts_dir}/03-wc.txt', 'w')
  run_command("printf 'aboba\nboba\n' | python3 03-wc.py", ofile)
  run_command("python3 03-wc.py 03-wc.py", ofile)
  ofile.close()

if __name__ == '__main__':
  main()
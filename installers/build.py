if __name__ == '__main__':
    import argparse
    from pathlib import Path
    import re
    import subprocess

    version_re = '\d+.\d+.\d+(.(a|b|rc|post)\d+)?'

    parser = argparse.ArgumentParser('build')
    parser.add_argument('version')
    args = parser.parse_args()

    construct_path = Path(__file__).parent / 'psiexperiment' / 'construct.yaml'
    text = construct_path.read_text()
    text = re.sub(f'(version: ){version_re}', f'\g<1>{args.version}', text)
    text = re.sub(f'(psiexperiment==){version_re}', f'\g<1>{args.version}', text)
    construct_path.write_text(text)

    cmd = ['constructor', '--platform', 'win-64', 'psiexperiment']
    subprocess.run(cmd)
    cmd = ['constructor', '--platform', 'win-32', 'psiexperiment']
    subprocess.run(cmd)

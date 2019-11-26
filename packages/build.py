if __name__ == '__main__':
    import argparse
    import hashlib
    from pathlib import Path
    import subprocess
    import re

    version_re = '\d+.\d+.\d+(.(a|b|rc|post)\d+)?'

    parser = argparse.ArgumentParser('build')
    parser.add_argument('version')
    parser.add_argument('source_path')
    args = parser.parse_args()

    source_path = Path(args.source_path)
    setup_path = source_path / 'setup.py'
    dist_path = source_path / 'dist'
    text = setup_path.read_text()
    text = re.sub(f"(version=)'{version_re}'", rf"\1'{args.version}'", text)
    setup_path.write_text(text)

     Build the pip package
    cmd = ['python', str(setup_path), 'sdist', 'bdist_wheel']
    subprocess.run(cmd)

    # Upload it
    cmd = ['twine', 'upload', str(dist_path) + '/*']
    subprocess.run(cmd)

    # Compute the hash and write relevant information to the meta.yaml file.
    bdist_file = dist_path / f'psiexperiment-{args.version}.tar.gz'
    bdist_hash = hashlib.sha256()
    bdist_hash.update(bdist_file.read_bytes())

    meta_path = Path(__file__).parent / 'psiexperiment' / 'meta.yaml'
    text = meta_path.read_text()
    text = re.sub(f'(version = )"{version_re}"', rf'\1"{args.version}"', text)
    text = re.sub('(sha256: )\w{64}', rf'\g<1>{bdist_hash.hexdigest()}', text)
    meta_path.write_text(text)

    # Build the conda package. It automatically gets uploaded as well.
    cmd = ['conda-build', 'psiexperiment']
    subprocess.run(cmd)

    # Cleanup.
    cmd = ['conda-build', 'purge']
    subprocess.run(cmd)

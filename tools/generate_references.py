import os
import argparse
import shutil


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--project', type=str, help='ClassIsland 仓库根目录', required=True)
    args = vars(parser.parse_args())
    script_workdir = os.getcwd()
    
    root = args['project']
    os.chdir(root)
    doc_root = os.path.join(script_workdir, "../docs/references")
    print("{} -> {}".format(root, doc_root))
    print("正在清理……")
    if (os.path.exists(doc_root)):
        shutil.rmtree(doc_root)
    os.mkdir(doc_root)
    
    print("正在生成解决方案……")
    os.system('dotnet build ./ClassIsland.sln -v q -p:WarningLevel=0')
    
    os.chdir(r".\ClassIsland.DocsGenerator\bin\Debug\net8.0-windows")
    
    print("正在生成文档……")
    os.system(r".\ClassIsland.DocsGenerator.exe ClassIsland.Core.dll {}/core --namespace ClassIsland --toc --skip-compiler-generated".format(doc_root))
    os.system(r".\ClassIsland.DocsGenerator.exe ClassIsland.Shared.dll {}/shared --namespace ClassIsland --toc --skip-compiler-generated".format(doc_root))
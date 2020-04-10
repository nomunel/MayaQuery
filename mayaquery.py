# coding:utf8

import os
import json
from pymel import core as pm


def import_loaded_references(remove_namespace=True):
    u'''
    loadしているReferenceを再帰的にimport（NestされたReferenceもimportします）
    remove_namespace: import時のnamespace削除有無（default:True）
    '''
    for loaded_reference in pm.listReferences(loaded=True):
        namespace = loaded_reference.fullNamespace
        loaded_reference.importContents()
        if namespace != ':' and remove_namespace:
            pm.namespace( removeNamespace=namespace, mergeNamespaceWithRoot=True )
            
    if pm.listReferences(loaded=True):
        import_loaded_references()

        
def load_json_file(path='', codec='utf_8_sig'):
    u'''
    JSONファイルをloadし、dict型でreturn
    codecは、utf-8以外で要指定（default値はutf8のDOM有無両対応）
    '''
    # TODO: output_text_fileの対になる関数名・挙動を検討（load_text_fileとして、拡張子がjsonなら～）
    result = {}
    if os.path.exists(path):
        with open(path) as f:
            result = json.loads(f.read().decode(encoding=codec))
    return result


def output_text_file(contents='', output_path=None):
    u'''
    - output_path未指定時、sceneファイルと同ディレクトリに'output.txt'出力
    - output_pathの拡張子が'.json'の場合、JSON形式で出力
    - contentsがlist型だった場合、要素ごとに改行
    '''
    if output_path is None:
        output_path = pm.workspace.getcwd() + 'output.txt'
    f = open(output_path, 'w') # ファイルを開く(該当ファイルがなければ新規作成)
    
    if output_path.endswith('.json'):
        contents = json.dumps(contents, indent=4, sort_keys=False)
        
    if type(contents) is list:
        for content in contents:
            f.write(str(content) + '\n')
    else:
        f.write(contents)
    f.close()

# coding:utf8

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
        import_objects_from_loaded_references()

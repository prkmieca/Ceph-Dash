from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('del/<poolName>', views.delPool, name='delPool'),
    path('add/', views.addPool, name="addPool"),
    path('edit/<poolName>/<poolType>', views.editPool, name='editPool'),
    path('quota/<poolName>', views.setQuota, name='setQuota'),
    path('snapshot/<poolName>', views.makeSnap, name='makeSnap'),
    path('rmsnapshot/<poolName>', views.removeSnap, name='removeSnap'),
    path('key/', views.osdSettings, name='osdSettings'),
    path('osd/reweight/<osdID>/<hostname>', views.reweight, name='reweight'),
    path('osd/repair/<osdID>/<hostname>', views.osdRepair, name='osdRepair'),
    path('osd/in/<osdID>/<hostname>', views.osdIn, name='osdIn'),
    path('osd/out/<osdID>/<hostname>', views.osdOut, name='osdOut'),
    path('osd/down/<osdID>/<hostname>', views.osdDown, name='osdDown'),
    path('osd/addErasure', views.addErasure, name='addErasure'),
    path('osd/delErasure/<erasure>', views.delErasure, name='delErasure'),
    path('osd/crush/addBucket', views.addBucket, name='addBucket'),
    path('osd/crush/addCrushRule', views.addCrushRule, name='addCrushRule'),
    path('osd/crush/moveHost', views.moveHost, name='moveHost'),
    path('osd/crush/delBucket', views.delBucket, name='delBucket'),
    path('osd/crush/delRule', views.delRule, name='delRule')
]
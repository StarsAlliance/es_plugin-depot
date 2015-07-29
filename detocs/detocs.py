# -*- coding:Utf-8 -*-

import es, playerlib, os, time, repeat, random, gamethread, langlib, urllib2

########NE PAS EDITER CE FICHIER########
########DON'T EDIT THIS FILE########

info = es.AddonInfo()
info.name = "DeToCs Anti-Cheat" 
info.version = "1.2"
info.author = "MegaMan" 
info.url = "www.team-tocs.com"

es.ServerVar('DeToCs', info.version, 'AntiCheat: Check cheating variables (by MegaMan)').makepublic()

action_on_cheatR = es.ServerVar("action_on_cheat")
ban_durationR = es.ServerVar("ban_duration")
ban_typeR = es.ServerVar("ban_type")
advert_on_cheatR = es.ServerVar("advert_on_cheat")
advert_on_nocheatR = es.ServerVar("advert_on_nocheat")
check_on_fragR = es.ServerVar("check_on_frag")
check_repeatR = es.ServerVar("check_repeat")
check_secondsR = es.ServerVar("check_seconds")
detocs_langR = es.ServerVar("detocs_lang")
ban_with_gbR = es.ServerVar("ban_with_gb")
idreason_gbR = es.ServerVar("idreason_gb")
steamid_gbR = es.ServerVar("steamid_gb")
detect = False
on_connect = False
messages = langlib.Strings(es.getAddonPath("detocs") + "/language.ini")

def load():
	es.log("[DeToCs] Load")
	es.server.cmd("es_xmexec ../addons/eventscripts/detocs/detocs.cfg")
	if int(check_repeatR) == 1:
		repeat.create("CheckCheat", check_variable_seconds)
		repeat.start("CheckCheat", int(check_secondsR), 0)

def unload():
	es.log("[DeToCs] Unload")
	if int(check_repeatR) == 1:
		repeat.stop("CheckCheat")
		repeat.delete("CheckCheat")

def player_activate(event_var):
	global on_connect
	if int(es.ServerVar("sv_cheats")) == 0:
		on_connect = True
		if int(check_on_fragR) == 0 and int(check_repeatR) == 0:
			check_variable_connect(event_var['userid'])
			gamethread.delayed(random.randint(40,100), check_variable, event_var['userid'])
		else:
			check_variable(event_var['userid'])

def check_variable(userid):
	global on_connect
	if int(es.ServerVar("sv_cheats")) == 0:
		if int(userid) in es.getUseridList():
			es.queryclientvar(userid, "sv_cheats")
			es.queryclientvar(userid, "mat_wireframe")
			es.queryclientvar(userid, "r_drawothermodels")
			es.queryclientvar(userid, "mat_fillrate")
			es.queryclientvar(userid, "snd_show")
			es.queryclientvar(userid, "snd_visualize")
			es.queryclientvar(userid, "r_partition_level")
			es.queryclientvar(userid, "r_drawbrushmodels")
			es.queryclientvar(userid, "mem_force_flush")
			es.queryclientvar(userid, "r_drawmodelstatsoverlay")
			es.queryclientvar(userid, "cl_leveloverview")
			es.queryclientvar(userid, "r_shadowwireframe")
			es.queryclientvar(userid, "r_visualizetraces")
			es.queryclientvar(userid, "r_rainspeed")
			es.queryclientvar(userid, "r_visualizelighttraces")
			es.queryclientvar(userid, "r_drawparticles")
			es.queryclientvar(userid, "r_drawlights")
			es.queryclientvar(userid, "r_drawrenderboxes")
			es.queryclientvar(userid, "vcollide_wireframe")
			es.queryclientvar(userid, "fog_enable")
			es.queryclientvar(userid, "mat_normalmaps")
			es.queryclientvar(userid, "mat_luxels")
			es.queryclientvar(userid, "cl_pitchup")
			es.queryclientvar(userid, "cl_pitchdown")
			es.queryclientvar(userid, "cl_bobcycle")
			es.queryclientvar(userid, "r_modelwireframedecal")
			es.queryclientvar(userid, "sv_showplayerhitboxes")
			es.queryclientvar(userid, "vgui_drawtree")
			if int(es.ServerVar("sv_consistency")) == 1:
				es.queryclientvar(userid, "sv_consistency")
			es.queryclientvar(userid, "mat_showlowresimage")
			on_connect = False
			es.queryclientvar(userid, "host_framerate")


def check_variable_connect(userid):
	es.queryclientvar(userid, "sv_cheats")
	es.queryclientvar(userid, "mat_wireframe")
	es.queryclientvar(userid, "r_drawothermodels")
	es.queryclientvar(userid, "mat_fillrate")
	es.queryclientvar(userid, "snd_show")
	es.queryclientvar(userid, "snd_visualize")
	es.queryclientvar(userid, "r_partition_level")
	es.queryclientvar(userid, "r_drawbrushmodels")
	es.queryclientvar(userid, "mem_force_flush")
	es.queryclientvar(userid, "r_drawmodelstatsoverlay")
	es.queryclientvar(userid, "cl_leveloverview")
	es.queryclientvar(userid, "r_shadowwireframe")
	es.queryclientvar(userid, "r_visualizetraces")
	es.queryclientvar(userid, "r_rainspeed")
	es.queryclientvar(userid, "r_visualizelighttraces")
	es.queryclientvar(userid, "r_drawparticles")
	es.queryclientvar(userid, "r_drawlights")
	es.queryclientvar(userid, "r_drawrenderboxes")
	es.queryclientvar(userid, "vcollide_wireframe")
	es.queryclientvar(userid, "fog_enable")
	es.queryclientvar(userid, "mat_normalmaps")
	es.queryclientvar(userid, "mat_luxels")
	es.queryclientvar(userid, "cl_pitchup")
	es.queryclientvar(userid, "cl_pitchdown")
	es.queryclientvar(userid, "cl_bobcycle")
	es.queryclientvar(userid, "r_modelwireframedecal")
	es.queryclientvar(userid, "sv_showplayerhitboxes")
	es.queryclientvar(userid, "vgui_drawtree")
	es.queryclientvar(userid, "mat_showlowresimage")
	if int(es.ServerVar("sv_consistency")) == 1:
		es.queryclientvar(userid, "sv_consistency")
	es.queryclientvar(userid, "host_framerate")

def check_variable_seconds():
	global on_connect
	if int(es.ServerVar("sv_cheats")) == 0:
		for userid in es.getUseridList():
			es.queryclientvar(userid, "sv_cheats")
			es.queryclientvar(userid, "mat_wireframe")
			es.queryclientvar(userid, "r_drawothermodels")
			es.queryclientvar(userid, "mat_fillrate")
			es.queryclientvar(userid, "snd_show")
			es.queryclientvar(userid, "snd_visualize")
			es.queryclientvar(userid, "r_partition_level")
			es.queryclientvar(userid, "r_drawbrushmodels")
			es.queryclientvar(userid, "mem_force_flush")
			es.queryclientvar(userid, "r_drawmodelstatsoverlay")
			es.queryclientvar(userid, "cl_leveloverview")
			es.queryclientvar(userid, "r_shadowwireframe")
			es.queryclientvar(userid, "r_visualizetraces")
			es.queryclientvar(userid, "r_rainspeed")
			es.queryclientvar(userid, "r_visualizelighttraces")
			es.queryclientvar(userid, "r_drawparticles")
			es.queryclientvar(userid, "r_drawlights")
			es.queryclientvar(userid, "r_drawrenderboxes")
			es.queryclientvar(userid, "vcollide_wireframe")
			es.queryclientvar(userid, "fog_enable")
			es.queryclientvar(userid, "mat_normalmaps")
			es.queryclientvar(userid, "mat_luxels")
			es.queryclientvar(userid, "cl_pitchup")
			es.queryclientvar(userid, "cl_pitchdown")
			es.queryclientvar(userid, "cl_bobcycle")
			es.queryclientvar(userid, "r_modelwireframedecal")
			es.queryclientvar(userid, "sv_showplayerhitboxes")
			es.queryclientvar(userid, "vgui_drawtree")
			es.queryclientvar(userid, "mat_showlowresimage")
			if int(es.ServerVar("sv_consistency")) == 1:
				es.queryclientvar(userid, "sv_consistency")
			on_connect = False
			es.queryclientvar(userid, "host_framerate")

def player_death(event_var):
	if int(check_on_fragR) == 1 and int(es.ServerVar("sv_cheats")) == 0:
		check_variable(event_var['attacker'])

def player_disconnect(event_var):
	global detect
	detect = False

def es_player_variable(event_var):
	global detect
	global on_connect
	variable_offense = False
	tokens = {}
	if (not detect) and (event_var['variable'] != "rate"):
		if (event_var['variable'] in "sv_cheats mat_wireframe mat_fillrate snd_show snd_visualize mem_force_flush r_drawmodelstatsoverlay cl_leveloverview r_shadowwireframe r_visualizetraces r_visualizelighttraces cl_particles_show_bbox r_drawlights r_drawrenderboxes vcollide_wireframe mat_normalmaps mat_luxels r_modelwireframedecal sv_showplayerhitboxes vgui_drawtree mat_showlowresimage") and (str(event_var['value']) != '0'):
			variable_offense = True
		elif (event_var['variable'] in "sv_consistency r_drawothermodels r_drawbrushmodels r_drawparticles fog_enable") and (str(event_var['value']) != '1'):
			variable_offense = True
		elif (event_var['variable'] == "cl_pitchup cl_pitchdown") and (str(event_var['value']) != '89'):
			variable_offense = True
		elif (event_var['variable'] == "r_partition_level") and (str(event_var['value']) != '-1'):
			variable_offense = True
		elif (event_var['variable'] == "cl_bobcycle") and (str(event_var['value']) != '0.8'):
			variable_offense = True
		elif (event_var['variable'] == "r_rainspeed") and (str(event_var['value']) != '600.0f'):
			variable_offense = True
		elif (event_var['variable'] == "host_framerate") and (str(event_var['value']) != '0'):
			joueur = playerlib.getPlayer(event_var['userid'])
			es.server.queuecmd("kickid %s [DeToCs] %s"%(event_var['userid'], messages("host_framerate",lang=joueur.get("lang"))))
			on_connect = False
		if variable_offense:
			tokens["variablecl"] = event_var['variable']
			tokens["userid"] = event_var['userid']
			tokens["username"] = es.getplayername(event_var['userid'])
			tokens["steamid"] = es.getplayersteamid(event_var['userid'])
			player = playerlib.getPlayer(event_var['userid'])
			userIp = player.attributes["address"]
			ipAddy, port = userIp.split(":")
			if int(action_on_cheatR) == 0:
				es.msg("#multi", messages("advert_cheat",opts=tokens,lang=detocs_langR))
				detect = True
			if int(action_on_cheatR) == 1:
				es.server.queuecmd("kickid %s [DeToCs] Kick (%s bypass)" % (event_var['userid'], event_var['variable']))
				detect = True
			elif int(action_on_cheatR) == 2:
				es.server.queuecmd("kickid %s [DeToCs] Ban (%s bypass)" % (event_var['userid'], event_var['variable']))
				if int(ban_with_gbR) == 1:
					es.server.queuecmd('es gb_externalBanUser "%s" "%s" %s %s minutes %s'%(str(steamid_gbR), es.getplayersteamid(event_var['userid']), str(idreason_gbR), str(ban_durationR), urllib2.quote(es.getplayername(event_var['userid']))))
					es.log("COMMANDE: es gb_externalBanUser %s %s %s %s minutes %s"%(str(steamid_gbR), es.getplayersteamid(event_var['userid']), str(idreason_gbR), str(ban_durationR), urllib2.quote(es.getplayername(event_var['userid']))))
				else:
					if int(ban_typeR) == 0:
						es.server.queuecmd("banid %s %s" % (int(es.ServerVar('ban_duration')), es.getplayersteamid(event_var['userid'])))
						es.server.queuecmd("writeid")
					elif int(ban_typeR) == 1:
						es.server.queuecmd("addip %s %s" % (int(es.ServerVar('ban_duration')), ipAddy))
						es.server.queuecmd("writeip")
					elif int(ban_typeR) == 2:
						es.server.queuecmd("addip %s %s" % (int(es.ServerVar('ban_duration')), ipAddy))
						es.server.queuecmd("banid %s %s" % (int(es.ServerVar('ban_duration')), es.getplayersteamid(event_var['userid'])))
						es.server.queuecmd("writeid")
						es.server.queuecmd("writeip")
				detect = True
			if (int(advert_on_cheatR) == 1) and (int(action_on_cheatR) == 1):
				es.msg ("#multi", messages("advert_kick",opts=tokens,lang=detocs_langR))
			elif (int(advert_on_cheatR) == 1) and (int(action_on_cheatR) == 2):
 				es.msg ("#multi", messages("advert_ban",opts=tokens,lang=detocs_langR))
			if os.path.isfile(os.getcwd() + "/cstrike/addons/eventscripts/detocs/detocs_logs.txt"):
				fichier = open(os.getcwd() + "/cstrike/addons/eventscripts/detocs/detocs_logs.txt", "a")
			else:
				fichier = open(os.getcwd() + "/cstrike/addons/eventscripts/detocs/detocs_logs.txt", "w")
			fichier.write("Date: %s %s\n"%(time.strftime("%d/%m/%y", time.localtime()), time.strftime("%H:%M", time.localtime())))
        		fichier.write("Username: %s\n"%es.getplayername(event_var['userid']))
        		fichier.write("SteamID: %s\n"%es.getplayersteamid(event_var['userid']))
        		fichier.write("IP: %s\n"%ipAddy)
			fichier.write("Variable: %s\n"%event_var['variable'])
			fichier.write("-----------------------------------\n")
       			fichier.close()
		elif (int(advert_on_nocheatR) == 1) and (event_var['variable'] == "host_framerate") and on_connect:
			tokens["username"] = es.getplayername(event_var['userid'])
			tokens["steamid"] = es.getplayersteamid(event_var['userid'])
			es.msg ("#multi", messages("advert_nocheat",opts=tokens,lang=detocs_langR))
			on_connect = False
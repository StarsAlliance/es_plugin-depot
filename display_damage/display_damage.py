import es
import cfglib
import usermsg


info = es.AddonInfo()
info.name = 'Display Damage'
info.version = 1.1
info.basename = 'display_damage'
info.url = 'http://addons.eventscripts.com/addons/view/display_damage'
info.author = 'Dead Man Walker'

AVAILABEL_AREAS = [
 'chat',
 'hudhint',
 'keyhint',
 'center'
]

cfg = cfglib.AddonCFG(es.ServerVar('eventscripts_gamedir') + "/cfg/" + info.basename + ".cfg")
cfg.text("*****************************************************************")
cfg.text("*** %s Config" %info.name)
cfg.text("*****************************************************************")
cfg.text(' ')
DISPLAY_DAMAGE_NAME = cfg.cvar('display_damage_name', 1, 'Show the name of the damaged player. 1=on, 0=off')
DISPLAY_DAMAGE_DISPLAY = cfg.cvar('display_damage_display', 'chat;keyhint;hudhint;center', 'Area(s) the damage will be displayed in. Seperate with a semicolon (;). See the list of available areas below')
cfg.text(' ')
cfg.text('Availabel display areas:')
for item in AVAILABEL_AREAS:
   cfg.text(' -' + item)
cfg.write()
cfg.execute()

def player_hurt(event_var):
   victim_id = int(event_var['userid'])
   damage = int(event_var['dmg_health'])
   attacker_id = int(event_var['attacker'])
   victim_name = event_var['es_username']
   attacker_name = event_var['es_attackername']
   if victim_id not in (0, attacker_id):
      display_areas_split = str(DISPLAY_DAMAGE_DISPLAY).strip().split(';')
      show_dmg = '-%sHP' %damage
      show_maxlen = max(len(victim_name), len(show_dmg))
      if int(DISPLAY_DAMAGE_NAME):
         show_msg = '%s\n%s' %(victim_name.center(show_maxlen), show_dmg.center(show_maxlen))
      else:
         show_msg = show_dmg
      if 'chat' in display_areas_split:
         es.tell(attacker_id, '#multi', '#green[DMG] #lightgreen%s' %show_msg)
      if 'hudhint' in display_areas_split:
         usermsg.hudhint(attacker_id, show_msg)
      if 'keyhint' in display_areas_split:
         usermsg.keyhint(attacker_id, show_msg)
      if 'center' in display_areas_split:
         es.centertell(attacker_id, show_msg)
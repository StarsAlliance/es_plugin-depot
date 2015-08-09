"""
This file is part of GlobalBan.

Written by Stefan Jonasson <soynuts@unbuinc.net>
Copyright 2008 Stefan Jonasson

GlobalBan is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

GlobalBan is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with GlobalBan.  If not, see <http://www.gnu.org/licenses/>.

*** DO NOT MODIFY ANYTHING IN THIS SCRIPT UNLESS YOU KNOW WHAT YOU ARE DOING ***

This script allows for easy banning of a user.  Once banned, the user can
be un-banned from the web-application as the ban is stored inside of a mysql
database.  Also, if the user attempts to join the server, they will get auto-kicked
as it will do a check against the mysql database to see if they exist and if
their ban period has yet to expire.  When the user has been banned on once server,
the user will be banned on all servers that are stored within the mysql table
that contains the servers that are running.  The script must be intalled in all
servers and the server ID must match the ID inside of the servers mysql table.


To ban, simply type !banmenu in say mode.  This will first let you select a
ban reason, followed by a ban length, and then finally the user to ban.  The
command is hidden from say and can not be seen by the public and is only
accessible by those found in the clan_db script.


For developers that wish to integrate GlobalBan into their script, please call
the regcmd gb_externalBanUser.  To execute it, do the following from your script:
  es gb_externalBanUser <adminUserId/adminSteamId> <steamIdToBan> <reasonIdOfBan> <lengthOfBan> <timeScale> <nameOfBanned>
The following is an example:
The admin with userid of 432 is banning the user with Steam ID STEAM_0:0:111111 for reason id 1 forever
Timescale can be in minutes, hours, days, weeks, or months
  es gb_externalBanUser 432 "STEAM_0:0:111111" 1 0 minutes myg0t
  es gb_externalBanUser "STEAM_0:0:000001" "STEAM_0:0:111111" 1 0 minutes myg0t

For scripts that automatically ban, you will want to use the following command:
The IP field is an optional field and is not required
  es gb_consoleBanUser <steamIdToBan> <banReasonId> <lengthOfBanInMinutes> <nameOfBanned> <ipOfBanned>
The following is an example:
  gb_consoleBanUser "STEAM_0:0:000000" 1 60 Test
This will ban Test who is identified by steam id STEAM_0:0:000000 for 60 minutes for ban reason #1.

*** Note: You must have quotes around steam ids ***


The following MUST be placed inside of your autoexec.cfg file.
es_load GlobalBan

Requirements:
PHP 4 or 5
MySQL 4.1+ or 5+
EventScripts v2.0+
"""
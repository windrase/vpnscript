from cybervpn import *

@bot.on(events.NewMessage(pattern=r"(?:.raikazu|/start|/raikazu)$"))
@bot.on(events.CallbackQuery(data=b'start'))
async def start(event):
	inline = [
[Button.inline("🔥 CREATE ACCOUNT 🔥","menu")],
[Button.url("GRUB","https://t.me/WintunelingVPNN")],
[Button.url("WHATSHAPP","https://wa.me/6285921645742")],
[Button.url("ORDER SCRIPT","https://t.me/WintunelingVPNN")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Akses Ditolak REGIS KE @WintunelingVPNN", alert=True)
		except:
			await event.reply("Akses Ditolak REGIS KE @WintunelingVPNN")
	elif val == "true":
		sdss = f" cat /etc/os-release | grep -w PRETTY_NAME | head -n1 | sed 's/=//g' | sed 's/PRETTY_NAME//g'"
		namaos = subprocess.check_output(sdss, shell=True).decode("ascii")
		ipvps = f" curl -s ipv4.icanhazip.com"
		ipsaya = subprocess.check_output(ipvps, shell=True).decode("ascii")
		citsy = f" cat /etc/xray/city"
		city = subprocess.check_output(citsy, shell=True).decode("ascii")

		msg = f"""
◇━━━━━━━━━━━━━━━━━━━━━━━◇
   **🔥 ADMIN PANEL 🔥**
◇━━━━━━━━━━━━━━━━━━━━━━━◇
 **⚡» OS VPS :** `{namaos.strip().replace('"','')}`
 **⚡» REGION :** `{city.strip()}`
 **⚡» DOMAIN :** `{DOMAIN}`
 **⚡» IP VPS :** `{ipsaya.strip()}`
◇━━━━━━━━━━━━━━━━━━━━━━◇
"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)






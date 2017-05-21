from core.rule_core import *

class YunoModule:

	name = "annonreverts"
	hours = 1
	reverts_required = 1

	def run(self, title):
		site = pywikibot.Site()
		edits = op.createEditList(title)
		reverts = op.getRevertList(edits)

		ip_reverts = 0

		if len(reverts) >= self.reverts_required:
			for rev in reverts:
				reverter = pywikibot.User(site, title=rev["reverter"])
				victim = pywikibot.User(site, title=rev["victim"])

				if "autoconfirmed" not in victim.groups() or "autoconfirmed" not in reverter.groups():
					ip_reverts += 1

		if ip_reverts >= self.reverts_required:
			return True

		return False
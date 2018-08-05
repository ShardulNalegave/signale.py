
module.exports = {

	title: "Signale.py",
	description: "Elegant Console Logger For Python Command Line Apps",

	head: [

		["link", {rel: "icon", href: "/hero.png"}]

	],

	themeConfig: {

		repo: "ShardulNalegave/signale.py",
		repoLabel: "GitHub",

		docsRepo: "ShardulNalegave/signale.py",
		docsBranch: "master",
		docsDir: "docs",

		editLinks: true,
		editLinkText: "Edit This Page On GitHub",

		nav: [

			{text: "Home", link: "/"},
			{text: "Guide", link: "/docs/"}

		],

		search: true,
		lastUpdated: 'Last Updated',

		sidebar: {
			"/docs/": [
				{
					title: "Guide",
					collabsible: true,
					children: [
						["/docs/", "Introduction"],
						["/docs/getting-started.html", "Getting Started"],
						["/docs/loggers.html", "Default Loggers"],
						["/docs/formatters.html", "Text Formatters"],
						["/docs/custom.html", "Custom Loggers"],
						["/docs/scopes.html", "Scoped Loggers"],
						["/docs/customize.html", "Configure"],
						["/docs/api.html", "API"]
					]
				}
			]
		}

	},

	markdown: {

		lineNumbers: true

	}

}
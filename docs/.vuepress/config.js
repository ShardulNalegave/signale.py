
module.exports = {

	title: "Signale.py",
	description: "Elegant Console Logger For Python Command Line Apps",

	themeConfig: {

		nav: [

			{text: "Home", link: "/"},
			{text: "Guide", link: "/docs/"},

			{text: "GitHub", link: "https://github.com/ShardulNalegave/signale.py"}

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
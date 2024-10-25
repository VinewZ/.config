local luasnip = require("luasnip")

luasnip.add_snippets("go", {
  luasnip.parser.parse_snippet("gerr", [[
  if err != nil {
    $0
  }
  ]]),
})

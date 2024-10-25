local luasnip = require("luasnip")

luasnip.add_snippets("javascript", {
  luasnip.parser.parse_snippet("czcta", [[
  .to("#czmb-t-$1", .2, { scale: 1.03 }, "start")
  .to("#czmb-t-$1", .2, { scale: 1 })
  .to("#czmb-t-$1", .2, { scale: 1.03 })
  .to("#czmb-t-$1", .2, { scale: 1 })
  .repeatDelay(3)
  .repeat(-1)
  ]]),
})

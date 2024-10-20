vim.opt.clipboard = "unnamedplus"
vim.opt.title = true
vim.api.nvim_exec([[
  tnoremap <Esc> <C-\><C-N>
]], false)

vim.opt.shiftwidth = 2
vim.opt.tabstop = 2
vim.opt.softtabstop = 2
vim.opt.expandtab = true
vim.opt.scrolloff = 10
vim.opt.autoindent = true
vim.opt.smartindent = true
vim.opt.breakindent = true
vim.opt.wrap = false
vim.opt.wildignore:append({ "*/node_modules/*" })
vim.opt.termguicolors = true

vim.wo.relativenumber = true

vim.api.nvim_set_hl(0, "LineNrAbove", { fg = "#BDBDBD" })
vim.api.nvim_set_hl(0, "LineNr", { fg = "#FFFFFF", bold = true })
vim.api.nvim_set_hl(0, "LineNrBelow", { fg = "#BDBDBD" })

vim.opt.cursorline = true
vim.opt.cursorcolumn = true

vim.cmd [[
  highlight CursorLine guibg=#2c2c2c
  highlight CursorColumn guibg=#2c2c2c
]]

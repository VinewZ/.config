return {
  vim.keymap.set("n", "<leader>do", '<cmd>lua vim.diagnostic.open_float()<CR>', {}),
  vim.keymap.set("n", "<leader>d[", '<cmd>lua vim.diagnostic.goto_prev()<CR>', {}),
  vim.keymap.set("n", "<leader>d]", '<cmd>lua vim.diagnostic.open_float()<CR>', {}),
}

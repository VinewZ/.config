return {
  {
    "williamboman/mason.nvim",
    config = function()
      require("mason").setup()
    end,
  },
  {
    "williamboman/mason-lspconfig.nvim",
    config = function()
      require("mason-lspconfig").setup({
        ensure_installed = {
          "lua_ls",
          "ts_ls",
          "html",
          "cssls",
          "tailwindcss",
          "pylsp",
          "gopls",
        },
      })
    end,
  },
  {
    "neovim/nvim-lspconfig",
    config = function()
      local capabilities = require("cmp_nvim_lsp").default_capabilities()
      local lspconfig = require("lspconfig")

      -- List of language servers
      local servers = {
        "lua_ls", "ts_ls", "pylsp", "html", "cssls",
        "tailwindcss", "gopls",
      }

      -- Setup each server
      for _, server in ipairs(servers) do
        lspconfig[server].setup({
          capabilities = capabilities,
        })
      end

      -- Keybindings for LSP
      local keymap_opts = { noremap = true, silent = true }
      vim.keymap.set("n", "K", vim.lsp.buf.hover, keymap_opts)
      vim.keymap.set("n", "gd", vim.lsp.buf.definition, keymap_opts)
      vim.keymap.set("n", "gr", function()
        require("telescope.builtin").lsp_references({
          layout_strategy = "vertical",
        })
      end, keymap_opts)
      vim.keymap.set("n", "gi", function()
        require("telescope.builtin").lsp_implementations({
          layout_strategy = "vertical",
        })
      end, keymap_opts)
      vim.keymap.set("n", "<leader>ca", vim.lsp.buf.code_action, keymap_opts)
    end,
  }
}

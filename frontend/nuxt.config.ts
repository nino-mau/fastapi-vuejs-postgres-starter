// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-01-15',
  modules: ['@nuxt/eslint', '@nuxt/ui'],
  css: ['~/assets/css/main.css'],
  ssr: false,

  devtools: {
    enabled: true,
  },

  devServer: {
    host: '0.0.0.0',
  },

  eslint: {
    config: {
      stylistic: {
        commaDangle: 'never',
        braceStyle: '1tbs',
      },
    },
  },

  typescript: {
    tsConfig: {
      compilerOptions: {
        allowJs: true,
        checkJs: false,
      },
    },
  },
});

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../../AMIS/**/*.{html,js}"],
  theme: {
    extend: {
      screens: {
        print:{ raw : 'print' }
      }
    },
  },
  plugins: [
    // use form plugins
    require("@tailwindcss/forms"),
  ],
};

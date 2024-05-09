/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../../AMIS/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [
    // use form plugins
    require("@tailwindcss/forms"),
  ],
};

const gulp = require("gulp");
const inlineCss = require("gulp-inline-css");
const replace = require("gulp-replace");
const removeCode = require("gulp-remove-code");
// var premailer = require("gulp-premailer");
// var juice = require("gulp-juice");

function inlineStyles() {
  return gulp
    .src("index.html")
    .pipe(removeCode({ production: true }))
    .pipe(
      inlineCss({
        applyStyleTags: false,
        applyLinkTags: true,
        removeStyleTags: false,
        removeLinkTags: true,
        removeHtmlSelectors: true,
      }),
    )
    .pipe(gulp.dest("html/"));
}

function replaceMsoComments() {
  return gulp.src("html/index.html").pipe(gulp.dest("html/index1.html"));
}
// function inlineCssWithJuice() {
//   return gulp.src("./*.html").pipe(juice()).pipe(gulp.dest("dist"));
// }
// function inlineCssWithPremailer() {
//   return gulp.src("./*.html").pipe(premailer()).pipe(gulp.dest("dist"));
// }
gulp.task("default", gulp.series(inlineStyles, replaceMsoComments));

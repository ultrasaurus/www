module.exports = function (eleventyConfig) {
    // Alias `layout: post` to `layout: layouts/post.njk`
    eleventyConfig.addLayoutAlias("post", "layouts/post.njk");
    eleventyConfig.addLayoutAlias("base", "layouts/base.liquid");

    return {
        dir: {
            input: "./src",   // source files
            output: "./_site" // static site generated here
        }
    };
};
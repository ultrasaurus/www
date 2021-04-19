module.exports = function (eleventyConfig) {
    // Alias `layout: post` to `layout: layouts/post.njk`
    eleventyConfig.addLayoutAlias("post", "layouts/post.njk");
    eleventyConfig.addLayoutAlias("base", "layouts/base.liquid");
    // Copy the `uploads/` directory
    eleventyConfig.addPassthroughCopy("uploads");
    eleventyConfig.addPassthroughCopy("CNAME");

    return {
        passthroughFileCopy: true,
        dir: {
            input: "./src",   // source files
            output: "./_site" // static site generated here
        }
    };
};
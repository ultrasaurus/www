module.exports = function (eleventyConfig) {

    // via https://www.belter.io/eleventy-sass-workflow/
    // By default, anything listed in .gitignore or .eleventyignore will be 
    // ignored by eleventy's watch process. If the compiled CSS is ignored, 
    //eleventy --serve wouldn't rebuild of the html whenever sass is recompiled.
    //workaround: opt-out of eleventy inspecting .gitignore with the following
    eleventyConfig.setUseGitIgnore(false);

    // Alias `layout: post` to `layout: layouts/post.njk`
    eleventyConfig.addLayoutAlias("post", "layouts/post.liquid");
    eleventyConfig.addLayoutAlias("base", "layouts/base.liquid");
    // Copy the `uploads/` directory
    eleventyConfig.addPassthroughCopy("uploads");
    eleventyConfig.addPassthroughCopy("CNAME");

    eleventyConfig.addFilter('category', function (collection, category) {
        if (!category) return [];
        const filtered = collection.filter(item => item.data.category == category)
        return filtered;
    });


    return {
        passthroughFileCopy: true,
        dir: {
            input: "./src",   // source files
            output: "./_site" // static site generated here
        }
    };
};
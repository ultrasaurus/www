module.exports = function (eleventyConfig) {
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
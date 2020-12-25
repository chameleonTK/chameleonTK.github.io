function chunk(bigarray, size) {
    var arrayOfArrays = [];
    for (var i=0; i<bigarray.length; i+=size) {
         arrayOfArrays.push(bigarray.slice(i,i+size));
    }
    return (arrayOfArrays);
}

function slides(){
    var arr = jQuery(".su-carousel-slides");
    var key = "math-detective-camp"
    for(var i=0;i<arr.length;i++) {
        var d = jQuery(arr[i]);
        var images = d.find(".su-carousel-slide img");
        var texts = []
        for(var j=0;j<images.length;j++) {
            var dot = jQuery(images[j]).attr("src").split(".");
            texts.push(key+'/'+dot[3]+"."+dot[4])
        }
        console.log(texts)
        texts = chunk(texts, 3);
        
        for(var j=0;j<texts.length;j++) {
    //         console.log('{% include aligner.html images="'+texts[j]+'" column=1 %}')
        }
    }
}

function images() {
    var arr = jQuery(".su-custom-gallery-slide a");
    for(var i=0;i<arr.length;i++) {
        var d = jQuery(arr[i]);
        var dot = d.attr("href").split(".")
        var key = "math-detective-camp"
        var img = '{% include aligner.html images="'+key+'/'+dot[3]+"."+dot[4]+'" column=1 %}'
        console.log(img)
    }
}
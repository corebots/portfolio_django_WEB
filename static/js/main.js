//
// var controller = new ScrollMagic.Controller();
//
// // Parallax background
// new ScrollMagic.Scene({
//         triggerElement: "#parallax",
//         triggerHook: "onEnter",
//     })
//     .duration('200%')
//     .setTween("#parallax", {
//         backgroundPosition: "50% 100%",
//         ease: Linear.easeNone
//     })
//     //.addIndicators() // for debugging purposes
//     .addTo(controller);
//
//
// new ScrollMagic.Scene({
//         triggerElement: "#slidein",
//         triggerHook: "onLeave",
//     })
//     .setPin("#slidein")
//     //.addIndicators() // add indicators (requires plugin)
//     .addTo(controller);
//
// new ScrollMagic.Scene({
//         triggerElement: "#slidein2",
//         triggerHook: "onLeave",
//     })
//     .setPin("#slidein2")
//     //.addIndicators() // add indicators (requires plugin)
//     .addTo(controller);
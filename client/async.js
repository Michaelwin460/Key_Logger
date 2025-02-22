console.log("start");

function asyncfunc(callback) {
    // setTimeout(() => {
    //     console.log("mission acomplished");
    //     callback();
    // }, 2000);
    console.log('the insude');
    
}

asyncfunc(() => {
    console.log('mooving on');
});

console.log('end');

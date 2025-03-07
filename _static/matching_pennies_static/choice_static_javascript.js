
var start_time = new Date().getTime(); //time at the start of the page; used for time measurements
let first = true; //checks for first move
choice1 = true; //variable for the first action
var game_over = false; // flag if the game has ended or not
//variables for all buttons:
var button1_1 = document.getElementById('button1_1');
var button2_1 = document.getElementById('button2_1');
var button1_1_start = document.getElementById('button1_1_start');
var button2_1_start = document.getElementById('button2_1_start');
var button1_2 = document.getElementById('button1_2');
var button2_2 = document.getElementById('button2_2');
var button1_2_start = document.getElementById('button1_2_start');
var button2_2_start = document.getElementById('button2_2_start');
var simultaneous = false; //variable if moves are made simultaneous or not
//initialize both  "timer" object
timer = startTimer(60, "timer", function() {timeOut()}); //timer object
factor = startFactor(60, js_vars.delta, "factor", function() {}); //payoff factor object (percentage)
//style timer according to starting paused
document.getElementById("outer-circle").style.background = "#696969";
document.getElementById("timer").style.color = "#696969";
//pause timers at the beginning
pause_beginning = timer.pause();
pause_beginning_factor = factor.pause();
//define flags for internal logic (javascript only)
pause_timer_started = true; // flag if the timer is paused
beginning_timer = true; // flag if in the first 5s of the game
move_in_beginning = false; // flag if one move is done in the beginning phase
i_moved = false; //flag if this player has moved already

//table animations
document.getElementById('matrix1_heads').style.animation = 'none';
document.getElementById('matrix1_tails').style.animation = 'none';
document.getElementById('matrix2_heads').style.animation = 'none';
document.getElementById('matrix2_tails').style.animation = 'none';

//displays the correct start matrix for each player
if(js_vars.player_id == 1){
    document.getElementById("payoff_matrix_1_start").style.display = "block";
}
if(js_vars.player_id == 2){
    document.getElementById("payoff_matrix_2_start").style.display = "block";
}

//end of stop function: incorporated all functionality if the 5s stop ends. This is called whenever a stop ends.
const end_of_stop = function() {
                        document.getElementById('timebar').classList.remove('active-animation'); //remove animation after 5 seconds
                        if(game_over == false){ //not both players have moved after initial pause
                            document.getElementById("outer-circle").style.background = "#159421";
                            document.getElementById("timer").style.color = "#159421";
                            timer.resume();
                            if(!i_moved){
                                factor.resume();
                            }
                        }
                        pause_timer_started=false;
                        }

//5sec stop time at beginning (Initialize the stop of the timer at the beginning. Note that during this time a move of
// an opponent can not be observed. Therefore, two different matrices exist for each player.
document.getElementById('timebar').classList.add('active-animation'); //run stop animation
setTimeout(function(){ // this function checks if both players moved in the first 5s. If not, they get displayed the regular matrix showing possible moves made
    if(game_over) { // both players moved in the beginning
        document.getElementById('simultaneous').value = true;
        document.getElementById('submit').style.display='inline';
        document.getElementById("outer-circle").style.background = "#696969";
        document.getElementById("timer").style.color = "#696969";
        document.getElementById("timebar").style.display = "none"
    }
    end_of_stop();
    beginning_timer = false;
},5000);


//live receive function
function liveRecv(data) {
    if (data['type'] == 'button'){
        if (data['first']) { //first move in the game
            first = false; //set fist flag to false for the second response
            if(beginning_timer == false){
                    if(js_vars.player_id == data['player']) { //if you are the first mover
                        factor.pause();
                    }
            }
            else{
                move_in_beginning = true;
            }
            if (data['player'] == 1) {
                if (data['penny_side']) {
                    choice1 = data['penny_side'];
                    console.log("player 1 first heads");
                    document.getElementById('matrix2_heads').style.animation = 'mymove 1.5s 1';

                    document.getElementById('tbl1_a2').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl1_b2').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl1_c2').style.backgroundColor='#f0c0c0';
                    document.getElementById('tails_text_1').style.color='#858585';
                    document.getElementById('tbl1_b3').style.color='#858585';
                    document.getElementById('tbl1_b3text').style.color='#858585';
                    document.getElementById('tbl1_c3').style.color='#858585';
                    document.getElementById('tbl1_c3text').style.color='#858585';
                    document.getElementById('tbl1_a2_start').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl1_b2_start').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl1_c2_start').style.backgroundColor='#f0c0c0';
                    document.getElementById('tails_text_1_start').style.color='#858585';
                    document.getElementById('tbl1_b3_start').style.color='#858585';
                    document.getElementById('tbl1_b3text_start').style.color='#858585';
                    document.getElementById('tbl1_c3_start').style.color='#858585';
                    document.getElementById('tbl1_c3text_start').style.color='#858585';

                    document.getElementById('tbl2_c1').style.color='#858585';
                    document.getElementById('tbl2_c2').style.color='#858585';
                    document.getElementById('tbl2_c2text').style.color='#858585';
                    document.getElementById('tbl2_c3').style.color='#858585';
                    document.getElementById('tbl2_c3text').style.color='#858585';
                    document.getElementById('tbl2_b1').style.borderTopWidth = "4px";
                    document.getElementById('tbl2_b1').style.borderRightWidth = "4px";
                    document.getElementById('tbl2_b1').style.borderLeftWidth = "4px";
                    document.getElementById('tbl2_b2').style.borderRightWidth = "4px";
                    document.getElementById('tbl2_b2').style.borderLeftWidth = "4px";
                    document.getElementById('tbl2_b3').style.borderRightWidth = "4px";
                    document.getElementById('tbl2_b3').style.borderLeftWidth = "4px";
                    document.getElementById('tbl2_b3').style.borderBottomWidth = "4px";

                } else {
                    choice1 = data['penny_side'];
                    console.log("player 1 first tails");
                    document.getElementById('matrix2_tails').style.animation = 'mymove 1.5s 1';

                    document.getElementById('tbl1_a3').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl1_b3').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl1_c3').style.backgroundColor='#f0c0c0';
                    document.getElementById('heads_text_1').style.color='#858585';
                    document.getElementById('tbl1_b2').style.color='#858585';
                    document.getElementById('tbl1_b2text').style.color='#858585';
                    document.getElementById('tbl1_c2').style.color='#858585';
                    document.getElementById('tbl1_c2text').style.color='#858585';
                    document.getElementById('tbl1_a3_start').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl1_b3_start').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl1_c3_start').style.backgroundColor='#f0c0c0';
                    document.getElementById('heads_text_1_start').style.color='#858585';
                    document.getElementById('tbl1_b2_start').style.color='#858585';
                    document.getElementById('tbl1_b2text_start').style.color='#858585';
                    document.getElementById('tbl1_c2_start').style.color='#858585';
                    document.getElementById('tbl1_c2text_start').style.color='#858585';

                    document.getElementById('tbl2_b1').style.color='#858585';
                    document.getElementById('tbl2_b2').style.color='#858585';
                    document.getElementById('tbl2_b2text').style.color='#858585';
                    document.getElementById('tbl2_b3').style.color='#858585';
                    document.getElementById('tbl2_b3text').style.color='#858585';
                    document.getElementById('tbl2_c1').style.borderTopWidth = "4px";
                    document.getElementById('tbl2_c1').style.borderRightWidth = "4px";
                    document.getElementById('tbl2_c1').style.borderLeftWidth = "4px";
                    document.getElementById('tbl2_c2').style.borderRightWidth = "4px";
                    document.getElementById('tbl2_c2').style.borderLeftWidth = "4px";
                    document.getElementById('tbl2_c3').style.borderRightWidth = "4px";
                    document.getElementById('tbl2_c3').style.borderLeftWidth = "4px";
                    document.getElementById('tbl2_c3').style.borderBottomWidth = "4px";
                }
            console.log("choice1:" +  choice1);
            }
            if (data['player'] == 2) {
                if (data['penny_side']) {
                    choice1 = data['penny_side'];
                    console.log("player 2 first heads");
                    document.getElementById('matrix1_heads').style.animation = 'mymove 1.5s 1';

                    document.getElementById('tbl2_a2').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl2_b2').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl2_c2').style.backgroundColor='#f0c0c0';
                    document.getElementById('tails_text_2').style.color='#858585';
                    document.getElementById('tbl2_b3').style.color='#858585';
                    document.getElementById('tbl2_b3text').style.color='#858585';
                    document.getElementById('tbl2_c3').style.color='#858585';
                    document.getElementById('tbl2_c3text').style.color='#858585';
                    document.getElementById('tbl2_a2_start').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl2_b2_start').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl2_c2_start').style.backgroundColor='#f0c0c0';
                    document.getElementById('tails_text_2_start').style.color='#858585';
                    document.getElementById('tbl2_b3_start').style.color='#858585';
                    document.getElementById('tbl2_b3text_start').style.color='#858585';
                    document.getElementById('tbl2_c3_start').style.color='#858585';
                    document.getElementById('tbl2_c3text_start').style.color='#858585';

                    document.getElementById('tbl1_c1').style.color='#858585';
                    document.getElementById('tbl1_c2').style.color='#858585';
                    document.getElementById('tbl1_c2text').style.color='#858585';
                    document.getElementById('tbl1_c3').style.color='#858585';
                    document.getElementById('tbl1_c3text').style.color='#858585';
                    document.getElementById('tbl1_b1').style.borderTopWidth = "4px";
                    document.getElementById('tbl1_b1').style.borderRightWidth = "4px";
                    document.getElementById('tbl1_b1').style.borderLeftWidth = "4px";
                    document.getElementById('tbl1_b2').style.borderRightWidth = "4px";
                    document.getElementById('tbl1_b2').style.borderLeftWidth = "4px";
                    document.getElementById('tbl1_b3').style.borderRightWidth = "4px";
                    document.getElementById('tbl1_b3').style.borderLeftWidth = "4px";
                    document.getElementById('tbl1_b3').style.borderBottomWidth = "4px";
                } else {
                    choice1 = data['penny_side'];
                    console.log("player 2 first tails");
                    document.getElementById('matrix1_tails').style.animation = 'mymove 1.5s 1';

                    document.getElementById('tbl2_a3').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl2_b3').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl2_c3').style.backgroundColor='#f0c0c0';
                    document.getElementById('heads_text_2').style.color='#858585';
                    document.getElementById('tbl2_b2').style.color='#858585';
                    document.getElementById('tbl2_b2text').style.color='#858585';
                    document.getElementById('tbl2_c2').style.color='#858585';
                    document.getElementById('tbl2_c2text').style.color='#858585';
                    document.getElementById('tbl2_a3_start').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl2_b3_start').style.backgroundColor='#f0c0c0';
                    document.getElementById('tbl2_c3_start').style.backgroundColor='#f0c0c0';
                    document.getElementById('heads_text_2_start').style.color='#858585';
                    document.getElementById('tbl2_b2_start').style.color='#858585';
                    document.getElementById('tbl2_b2text_start').style.color='#858585';
                    document.getElementById('tbl2_c2_start').style.color='#858585';
                    document.getElementById('tbl2_c2text_start').style.color='#858585';

                    document.getElementById('tbl1_b1').style.color='#858585';
                    document.getElementById('tbl1_b2').style.color='#858585';
                    document.getElementById('tbl1_b2text').style.color='#858585';
                    document.getElementById('tbl1_b3').style.color='#858585';
                    document.getElementById('tbl1_b3text').style.color='#858585';
                    document.getElementById('tbl1_c1').style.borderTopWidth = "4px";
                    document.getElementById('tbl1_c1').style.borderRightWidth = "4px";
                    document.getElementById('tbl1_c1').style.borderLeftWidth = "4px";
                    document.getElementById('tbl1_c2').style.borderRightWidth = "4px";
                    document.getElementById('tbl1_c2').style.borderLeftWidth = "4px";
                    document.getElementById('tbl1_c3').style.borderRightWidth = "4px";
                    document.getElementById('tbl1_c3').style.borderLeftWidth = "4px";
                    document.getElementById('tbl1_c3').style.borderBottomWidth = "4px";
                }
            }

        } else { //second move in game
                //if(pause_first_flag){
                //    clearTimeout(pause_first);
                //}
                if(pause_timer_started == false){
                    timer.pause();
                    if(js_vars.player_id == data['player']) { //if you are second mover
                        factor.pause();
                        }
                    }
                game_over = true;
                if(beginning_timer == false){
                    document.getElementById('submit').style.display='inline';
                    document.getElementById("outer-circle").style.background = "#696969";
                    document.getElementById("timer").style.color = "#696969";
                    document.getElementById("timebar").style.display = "none"
                }


                if(data['player'] == 1) { // player 1 is second mover
                    if (data['penny_side']) {// heads (second move)
                        console.log("player 1 second heads");
                        document.getElementById('matrix2_heads').style.animation = 'mymove 1.5s 1';
                        document.getElementById('tbl1_a2').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl1_b2').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl1_c2').style.backgroundColor='#f0c0c0';
                        document.getElementById('tails_text_1').style.color='#858585';
                        document.getElementById('tbl1_b3').style.color='#858585';
                        document.getElementById('tbl1_b3text').style.color='#858585';
                        document.getElementById('tbl1_c3').style.color='#858585';
                        document.getElementById('tbl1_c3text').style.color='#858585';
                        document.getElementById('tbl1_a2_start').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl1_b2_start').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl1_c2_start').style.backgroundColor='#f0c0c0';
                        document.getElementById('tails_text_1_start').style.color='#858585';
                        document.getElementById('tbl1_b3_start').style.color='#858585';
                        document.getElementById('tbl1_b3text_start').style.color='#858585';
                        document.getElementById('tbl1_c3_start').style.color='#858585';
                        document.getElementById('tbl1_c3text_start').style.color='#858585';

                        document.getElementById('tbl2_c1').style.color='#858585';
                        document.getElementById('tbl2_c2').style.color='#858585';
                        document.getElementById('tbl2_c2text').style.color='#858585';
                        document.getElementById('tbl2_c3').style.color='#858585';
                        document.getElementById('tbl2_c3text').style.color='#858585';
                        document.getElementById('tbl2_b1').style.borderTopWidth = "4px";
                        document.getElementById('tbl2_b1').style.borderRightWidth = "4px";
                        document.getElementById('tbl2_b1').style.borderLeftWidth = "4px";
                        document.getElementById('tbl2_b2').style.borderRightWidth = "4px";
                        document.getElementById('tbl2_b2').style.borderLeftWidth = "4px";
                        document.getElementById('tbl2_b3').style.borderRightWidth = "4px";
                        document.getElementById('tbl2_b3').style.borderLeftWidth = "4px";
                        document.getElementById('tbl2_b3').style.borderBottomWidth = "4px";
                        document.getElementById('tbl2_c3_start').style.color='#858585';
                        document.getElementById('tbl2_c3text_start').style.color='#858585';

                        if(choice1){
                            document.getElementById('tbl1_b2text').style.fontSize = "26px";
                            document.getElementById('tbl2_b2text').style.fontSize = "26px";
                        }
                        else{
                            document.getElementById('tbl1_c2text').style.fontSize = "26px";
                            document.getElementById('tbl2_b3text').style.fontSize = "26px";
                        }
                    }
                    else { // tails second move
                        console.log("player 1 second tails");
                        document.getElementById('matrix2_tails').style.animation = 'mymove 1.5s 1';
                        document.getElementById('tbl1_a3').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl1_b3').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl1_c3').style.backgroundColor='#f0c0c0';
                        document.getElementById('heads_text_1').style.color='#858585';
                        document.getElementById('tbl1_b2').style.color='#858585';
                        document.getElementById('tbl1_b2text').style.color='#858585';
                        document.getElementById('tbl1_c2').style.color='#858585';
                        document.getElementById('tbl1_c2text').style.color='#858585';
                        document.getElementById('tbl1_a3_start').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl1_b3_start').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl1_c3_start').style.backgroundColor='#f0c0c0';
                        document.getElementById('heads_text_1_start').style.color='#858585';
                        document.getElementById('tbl1_b2_start').style.color='#858585';
                        document.getElementById('tbl1_b2text_start').style.color='#858585';
                        document.getElementById('tbl1_c2_start').style.color='#858585';
                        document.getElementById('tbl1_c2text_start').style.color='#858585';

                        document.getElementById('tbl2_b1').style.color='#858585';
                        document.getElementById('tbl2_b2').style.color='#858585';
                        document.getElementById('tbl2_b2text').style.color='#858585';
                        document.getElementById('tbl2_b3').style.color='#858585';
                        document.getElementById('tbl2_b3text').style.color='#858585';
                        document.getElementById('tbl2_c1').style.borderTopWidth = "4px";
                        document.getElementById('tbl2_c1').style.borderRightWidth = "4px";
                        document.getElementById('tbl2_c1').style.borderLeftWidth = "4px";
                        document.getElementById('tbl2_c2').style.borderRightWidth = "4px";
                        document.getElementById('tbl2_c2').style.borderLeftWidth = "4px";
                        document.getElementById('tbl2_c3').style.borderRightWidth = "4px";
                        document.getElementById('tbl2_c3').style.borderLeftWidth = "4px";
                        document.getElementById('tbl2_c3').style.borderBottomWidth = "4px";

                        if(choice1){
                            document.getElementById('tbl1_b3text').style.fontSize = "26px";
                            document.getElementById('tbl2_c2text').style.fontSize = "26px";
                        }
                        else{
                            document.getElementById('tbl1_c3text').style.fontSize = "26px";
                            document.getElementById('tbl2_c3text').style.fontSize = "26px";
                        }
                    }
                }
                else{ //player two second mover
                     if (data['penny_side']) { //player two second heads
                        console.log("player 2 second heads");
                        document.getElementById('matrix1_heads').style.animation = 'mymove 1.5s 1';
                        document.getElementById('tbl2_a2').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl2_b2').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl2_c2').style.backgroundColor='#f0c0c0';
                        document.getElementById('tails_text_2').style.color='#858585';
                        document.getElementById('tbl2_b3').style.color='#858585';
                        document.getElementById('tbl2_b3text').style.color='#858585';
                        document.getElementById('tbl2_c3').style.color='#858585';
                        document.getElementById('tbl2_c3text').style.color='#858585';
                        document.getElementById('tbl2_a2_start').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl2_b2_start').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl2_c2_start').style.backgroundColor='#f0c0c0';
                        document.getElementById('tails_text_2_start').style.color='#858585';
                        document.getElementById('tbl2_b3_start').style.color='#858585';
                        document.getElementById('tbl2_b3text_start').style.color='#858585';
                        document.getElementById('tbl2_c3_start').style.color='#858585';
                        document.getElementById('tbl2_c3text_start').style.color='#858585';

                        document.getElementById('tbl1_c1').style.color='#858585';
                        document.getElementById('tbl1_c2').style.color='#858585';
                        document.getElementById('tbl1_c2text').style.color='#858585';
                        document.getElementById('tbl1_c3').style.color='#858585';
                        document.getElementById('tbl1_c3text').style.color='#858585';
                        document.getElementById('tbl1_b1').style.borderTopWidth = "4px";
                        document.getElementById('tbl1_b1').style.borderRightWidth = "4px";
                        document.getElementById('tbl1_b1').style.borderLeftWidth = "4px";
                        document.getElementById('tbl1_b2').style.borderRightWidth = "4px";
                        document.getElementById('tbl1_b2').style.borderLeftWidth = "4px";
                        document.getElementById('tbl1_b3').style.borderRightWidth = "4px";
                        document.getElementById('tbl1_b3').style.borderLeftWidth = "4px";
                        document.getElementById('tbl1_b3').style.borderBottomWidth = "4px";

                        if(choice1){
                            document.getElementById('tbl1_b2text').style.fontSize = "26px";
                            document.getElementById('tbl2_b2text').style.fontSize = "26px";
                        }
                        else{
                            document.getElementById('tbl1_b3text').style.fontSize = "26px";
                            document.getElementById('tbl2_c2text').style.fontSize = "26px";
                        }
                     }
                    else{ //player two second tails
                        console.log("player 2 second tails");
                        document.getElementById('matrix1_tails').style.animation = 'mymove 1.5s 1';
                        document.getElementById('tbl2_a3').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl2_b3').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl2_c3').style.backgroundColor='#f0c0c0';
                        document.getElementById('heads_text_2').style.color='#858585';
                        document.getElementById('tbl2_b2').style.color='#858585';
                        document.getElementById('tbl2_b2text').style.color='#858585';
                        document.getElementById('tbl2_c2').style.color='#858585';
                        document.getElementById('tbl2_c2text').style.color='#858585';
                        document.getElementById('tbl2_a3_start').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl2_b3_start').style.backgroundColor='#f0c0c0';
                        document.getElementById('tbl2_c3_start').style.backgroundColor='#f0c0c0';
                        document.getElementById('heads_text_2_start').style.color='#858585';
                        document.getElementById('tbl2_b2_start').style.color='#858585';
                        document.getElementById('tbl2_b2text_start').style.color='#858585';
                        document.getElementById('tbl2_c2_start').style.color='#858585';
                        document.getElementById('tbl2_c2text_start').style.color='#858585';

                        document.getElementById('tbl1_b1').style.color='#858585';
                        document.getElementById('tbl1_b2').style.color='#858585';
                        document.getElementById('tbl1_b2text').style.color='#858585';
                        document.getElementById('tbl1_b3').style.color='#858585';
                        document.getElementById('tbl1_b3text').style.color='#858585';
                        document.getElementById('tbl1_c1').style.borderTopWidth = "4px";
                        document.getElementById('tbl1_c1').style.borderRightWidth = "4px";
                        document.getElementById('tbl1_c1').style.borderLeftWidth = "4px";
                        document.getElementById('tbl1_c2').style.borderRightWidth = "4px";
                        document.getElementById('tbl1_c2').style.borderLeftWidth = "4px";
                        document.getElementById('tbl1_c3').style.borderRightWidth = "4px";
                        document.getElementById('tbl1_c3').style.borderLeftWidth = "4px";
                        document.getElementById('tbl1_c3').style.borderBottomWidth = "4px";

                         if(choice1){
                            document.getElementById('tbl1_c2text').style.fontSize = "26px";
                            document.getElementById('tbl2_b3text').style.fontSize = "26px";
                        }
                        else{
                            document.getElementById('tbl1_c3text').style.fontSize = "26px";
                            document.getElementById('tbl2_c3text').style.fontSize = "26px";
                        }
                     }
            }
            if(js_vars.player_id == 1) { //display correct matrix after game is over
                document.getElementById("payoff_matrix_1_start").style.display = "none";
                document.getElementById("payoff_matrix_1").style.display = "block";
            }
            if(js_vars.player_id == 2) { //display correct matrix after game is over
                document.getElementById("payoff_matrix_2_start").style.display = "none";
                document.getElementById("payoff_matrix_2").style.display = "block";
            }
        }
    }

}


// TIMER ON PAGE
function startTimer(seconds, container, oncomplete) { //function to create timer object
    var startTime, timer, obj, ms = seconds*1000,
        display = document.getElementById(container);
    obj = {};
    obj.resume = function() {
        startTime = new Date().getTime();
        timer = setInterval(obj.step,250); // adjust this number to affect granularity; lower numbers are more accurate, but more CPU-expensive
    };
    obj.pause = function() {
        ms = obj.step();
        clearInterval(timer);
    };
    obj.step = function() {
        var now = Math.max(0,ms-(new Date().getTime()-startTime)),
            s = Math.floor(now/1000)
        s = (s < 10 ? "0" : "")+s+"s";
        display.innerHTML = s;
        if( now == 0) {
            clearInterval(timer);
            obj.resume = function() {};
            if( oncomplete) oncomplete();
        }
        return now;
    };
    obj.resume();
    return obj;
}

function heads(){ //function called when heads is clicked
    if(js_vars.player_id == 1){
        button1_1.disabled = true;
        button2_1.disabled = true;
        button1_1_start.disabled = true;
        button2_1_start.disabled = true;
        button1_1.style.display = "none";
        document.getElementById("heads_text_1").style.display = "inline";
        button2_1.style.display = "none";
        document.getElementById("tails_text_1").style.display = "inline";
        button1_1_start.style.display = "none";
        document.getElementById("heads_text_1_start").style.display = "inline";
        button2_1_start.style.display = "none";
        document.getElementById("tails_text_1_start").style.display = "inline";
    }
    if(js_vars.player_id == 2){
        button1_2.disabled = true;
        button2_2.disabled = true;
        button1_2_start.disabled = true;
        button2_2_start.disabled = true;
        button1_2.style.display = "none";
        document.getElementById("heads_text_2").style.display = "inline";
        button2_2.style.display = "none";
        document.getElementById("tails_text_2").style.display = "inline";
        button1_2_start.style.display = "none";
        document.getElementById("heads_text_2_start").style.display = "inline";
        button2_2_start.style.display = "none";
        document.getElementById("tails_text_2_start").style.display = "inline";
    }
    var choice = true; //heads is true, tails is false
    var time_spent = Date.now() - start_time; //time between the initial loading of page and pressing the button
    i_moved = true;
    document.getElementById('time_of_move').value = time_spent; //manually fill otree form fields
    document.getElementById('penny_side').value = choice;
    document.getElementById('time_out').value = false;
    document.getElementById('move_in_beginning').value = beginning_timer;//move during the beginning
    document.getElementById('simultaneous').value = simultaneous;
    if(first) {
        liveSend({"type": "button", "penny_side": choice, "first": true}) //send information about first or second move and heads or tails to the server
    }
    else {
        liveSend({"type": "button", "penny_side": choice, "first": false})
    }
}

function tails(){ //similar to heads() above but called when tails is clicked instead
    if(js_vars.player_id == 1){
        button1_1.disabled = true;
        button2_1.disabled = true;
        button1_1_start.disabled = true;
        button2_1_start.disabled = true;
        button1_1.style.display = "none"
        document.getElementById("heads_text_1").style.display = "inline"
        button2_1.style.display = "none"
        document.getElementById("tails_text_1").style.display = "inline"
        document.getElementById("heads_text_1_start").style.display = "inline"
        button1_1_start.style.display = "none"
        document.getElementById("tails_text_1_start").style.display = "inline"
        button2_1_start.style.display = "none"
    }
    if(js_vars.player_id == 2){
        button1_2.disabled = true;
        button2_2.disabled = true;
        button1_2_start.disabled = true;
        button2_2_start.disabled = true;
        button1_2.style.display = "none"
        document.getElementById("heads_text_2").style.display = "inline"
        button2_2.style.display = "none"
        document.getElementById("tails_text_2").style.display = "inline"
        button1_2_start.style.display = "none"
        document.getElementById("heads_text_2_start").style.display = "inline"
        button2_2_start.style.display = "none"
        document.getElementById("tails_text_2_start").style.display = "inline"
    }
    var choice = false;
    var time_spent = Date.now() - start_time;
    i_moved = true;
    console.log('time_spent: ' + time_spent)
    document.getElementById('time_of_move').value = time_spent;
    document.getElementById('penny_side').value = choice;
    document.getElementById('time_out').value = false;
    document.getElementById('move_in_beginning').value = beginning_timer; //move during the beginning
    document.getElementById('simultaneous').value = simultaneous;
    if(first==true) {
        liveSend({"type": "button", "penny_side": choice, "first": true})
    }
    else {
        liveSend({"type": "button", "penny_side": choice, "first": false})
    }
}

//Timeout function
function timeOut() { //timeout function. This is called, when the timer runs out. Similar behaviour to heads()/tails() function
    button1_1.disabled = true;
    button2_1.disabled = true;
    button1_1_start.disabled = true;
    button2_1_start.disabled = true;

    button1_1.style.display = "none";
    document.getElementById("heads_text_1").style.display = "inline";
    button2_1.style.display = "none";
    document.getElementById("tails_text_1").style.display = "inline";
    button1_1_start.style.display = "none";
    document.getElementById("heads_text_1_start").style.display = "inline";
    button2_1_start.style.display = "none";
    document.getElementById("tails_text_1_start").style.display = "inline";

    button1_2.style.display = "none";
    document.getElementById("heads_text_2").style.display = "inline";
    button2_2.style.display = "none";
    document.getElementById("tails_text_2").style.display = "inline";
    button1_2_start.style.display = "none";
    document.getElementById("heads_text_2_start").style.display = "inline";
    button2_2_start.style.display = "none";
    document.getElementById("tails_text_2_start").style.display = "inline";
    if(i_moved == false) {
        document.getElementById('penny_side').value = true;
        document.getElementById('time_of_move').value = 65001;
        document.getElementById('time_out').value = true;
        document.getElementById('simultaneous').value = simultaneous;
        document.getElementById('move_in_beginning').value = beginning_timer; //move during the beginning
    }
    document.getElementById('submit').style.display='inline';
    document.getElementById("outer-circle").style.background = "#696969";
    document.getElementById("timer").style.color = "#696969";
}

// Dynamic payoff factor: analogue object as the timer. Displays the percentage of payoff received
function startFactor(seconds, delta, container, oncomplete) {
    var startTime, timer, obj, ms = seconds*1000,
        display = document.getElementById(container); //the html container where this is placed
    obj = {};
    obj.resume = function() {
        startTime = new Date().getTime();
        timer = setInterval(obj.step,100); // adjust this number to affect granularity
                            // lower numbers are more accurate, but more CPU-expensive
    };
    obj.pause = function() {
        ms = obj.step();
        clearInterval(timer);
    };
    obj.step = function() {
        var now = Math.max(0,ms-(new Date().getTime()-startTime));
        var factor = 1-(1-delta)*((60000-now)/60000);
        p = (factor * 100).toFixed(2) + "%";
        display.innerHTML = p;
        if( now == 0) {
            clearInterval(timer);
            obj.resume = function() {};
            if( oncomplete) oncomplete();
        }
        return now;
    };
    obj.resume();
    return obj;
}
let userScore = 0;
let computerScore = 0;

function playGame(userChoice) {

    const choices = ["snake", "water", "gun"];
    const computerChoice = choices[Math.floor(Math.random() * 3)];

    let message = "";

    if (userChoice === computerChoice) {
        message = "It's a Draw 😐";
    }
    else if (
        (userChoice === "snake" && computerChoice === "water") ||
        (userChoice === "water" && computerChoice === "gun") ||
        (userChoice === "gun" && computerChoice === "snake")
    ) {
        userScore++;
        message = "🎉 You Win!";
    }
    else {
        computerScore++;
        message = "😢 You Lose!";
    }

    document.getElementById("userScore").innerText = userScore;
    document.getElementById("computerScore").innerText = computerScore;

    document.getElementById("message").innerText =
        `You chose ${userChoice.toUpperCase()} | Computer chose ${computerChoice.toUpperCase()}  
${message}`;
}

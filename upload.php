<?php
  if ($_POST['chatbot_type'] == 'group') {
    $folder = 'group_chatbots/';
  } else if ($_POST['chatbot_type'] == 'single') {
    $folder = 'chatbots/';
  } else if ($_POST['chatbot_type'] == 'text_game') {
    $folder = 'text_game/';
  } else if ($_POST['chatbot_type'] == 'graphical') {
    $folder = 'graphical/';
  } else {
    $message = "<b>Error:</b> Chatbot type not specified - this is not your fault we screwed up.";
  }
  if (isset($folder)) {
    if ($_FILES["file"]["error"] > 0) {
      $message = "<b>Error: ".$_FILES["file"]["error"]."</b> Please select a file to upload.";
    } else {
      // echo "Upload: " . $_FILES["file"]["name"] . "<br>";
      // echo "Type: " . $_FILES["file"]["type"] . "<br>";
      // echo "Size: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
      // echo "Stored in: " . $_FILES["file"]["tmp_name"];
      $extension = end(explode(".", $_FILES["file"]["name"]));
      if ($extension !== 'py') {
        $message = "You must upload a valid .py file, not a ".$_FILES["file"]["type"]." .".$extension." file. Please try again.<br>";
      } else {
        $message = "Your file is OK and has been uploaded to $folder!<br>";
        move_uploaded_file($_FILES["file"]["tmp_name"], $folder.$_FILES["file"]["name"]);
      }
    }
  }
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="main.css">

    <script src="https://code.jquery.com/jquery.js"></script>
  </head>
  <body>
    <div class="container">
      <h1>Upload File Page</h1>
      <p class="lead"><?=$message?></p>
      <br>
      <a href="index.php">Return to chat</a>
    </div>
  </body>
</html>

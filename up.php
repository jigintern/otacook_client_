<?php
if (is_uploaded_file($_FILES["file"]["tmp_name"])) {
    $filename = "files/" .date("Ymd-His") . $_FILES["file"]["name"];
    if (move_uploaded_file ($_FILES["file"]["tmp_name"], $filename)) {
        chmod($filename, 0644);
        echo "https://t1.intern.jigd.info/".$filename;
    } else {
        echo "-1";
    }
} else {
    echo "-2";
}
?>
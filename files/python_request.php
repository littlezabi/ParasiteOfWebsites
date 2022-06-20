<?php 
$con = mysqli_connect('localhost', 'firmware_res', '7.JXD7wZXYU', 'firmware_res');
if(isset($_POST['bot_request'])){
    $action = $_POST['action'] ?? '';
    $url = $_POST['url'];
    $title = $_POST['title'] ?? '';
    $size = $_POST['size'] ?? '';
    $date = $_POST['date'] ?? date('Y-m-d');
    $description = $_POST['description'] ?? '';
    if(strlen($url) > 0){
        $srch_dup = $con->query("SELECT `url` FROM `res_files` WHERE `url` = '$url'");
        if($srch_dup->num_rows > 0){
            if ($action == 'update'){
                $query = "UPDATE `res_files` SET `title` = '$title', `description` = '$description', `size` = $size, `url` = '$url', `date_new` = CURRENT_TIMESTAMP WHERE `url` = '$url'";
                $sql = $con->query($query);
                if ($sql) exit('updated');
                else exit('Error');
            }
            else exit('AlreadyExist');
        }else{
            $sql = $con->query("INSERT INTO `res_files` (`title`, `description`, `size`, `url`, `is_active`, `is_new`, `is_featured`, `date_new`) VALUES ('$title', '$description', $size, '$url', 1, 1, 1, CURRENT_TIMESTAMP)");
            if ($sql) echo 'Success';
            else echo 'Error';
        }
    }
}











// $con = mysqli_connect('localhost', 'hcfirmwa_res', 'kx@6CoA3R3', 'hcfirmwa_res');
// if(isset($_POST['bot_request'])){
//     $action = $_POST['action'];
//     $url = $_POST['url'];
//     $title = $_POST['title'] ?? '';
//     $size = $_POST['size'] ?? '';
//     $date = $_POST['date'] ?? date('Y-m-d');
//     $description = $_POST['description'] ?? '';
//     if(strlen($url) > 0){
//         $srch_dup = $con->query("SELECT `url` FROM `hcf_files` WHERE `url` = '$url'");
//         if($srch_dup->num_rows > 0){
//             if ($action == 'update'){
//                 $query = "UPDATE `hcf_files` SET `title` = '$title', `description` = '$description', `size` = $size, `url` = '$url', `date_new` = CURRENT_TIMESTAMP WHERE `url` = '$url'";
//                 $sql = $con->query($query);
//                 if ($sql) exit('updated');
//                 else exit('Error');
//             }
//             else exit('AlreadyExist');
//         }else{
//             $sql = $con->query("INSERT INTO `hcf_files` (`title`, `description`, `size`, `url`, `is_active`, `is_new`, `is_featured`, `date_new`) VALUES ('$title', '$description', $size, '$url', 1, 1, 1, CURRENT_TIMESTAMP)");
//             if ($sql) echo 'Success';
//             else echo 'Error';
//         }
//     }
// }


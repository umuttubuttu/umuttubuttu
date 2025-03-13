
@{
    Layout = null;
}

<!DOCTYPE html>

<html>
<head>
    <link href="~/Content/bootstrap.min.css" rel="stylesheet" />
    <script src="~/Scripts/bootstrap.min.js"></script>
    <meta name="viewport" content="width=device-width" />
    <title>Resimler</title>
</head>
<body>
    <!-- Gallery -->
    <div class="row">
        <div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
            <img src="https://mdbcdn.b-cdn.net/img/Photos/Horizontal/Nature/4-col/img%20(73).webp"
                 class="w-100 shadow-1-strong rounded mb-4"
                 alt="Boat on Calm Water" />

            <img src="https://mdbcdn.b-cdn.net/img/Photos/Vertical/mountain1.webp"
                 class="w-100 shadow-1-strong rounded mb-4"
                 alt="Wintry Mountain Landscape" />
        </div>

        <div class="col-lg-4 mb-4 mb-lg-0">
            <img src="https://mdbcdn.b-cdn.net/img/Photos/Vertical/mountain2.webp"
                 class="w-100 shadow-1-strong rounded mb-4"
                 alt="Mountains in the Clouds" />

            <img src="https://mdbcdn.b-cdn.net/img/Photos/Horizontal/Nature/4-col/img%20(73).webp"
                 class="w-100 shadow-1-strong rounded mb-4"
                 alt="Boat on Calm Water" />
        </div>

        <div class="col-lg-4 mb-4 mb-lg-0">
            <img src="https://mdbcdn.b-cdn.net/img/Photos/Horizontal/Nature/4-col/img%20(18).webp"
                 class="w-100 shadow-1-strong rounded mb-4"
                 alt="Waves at Sea" />

            <img src="https://mdbcdn.b-cdn.net/img/Photos/Vertical/mountain3.webp"
                 class="w-100 shadow-1-strong rounded mb-4"
                 alt="Yosemite National Park" />
        </div>
    </div>
    <!-- Gallery -->
</body>
<center>
<div class="container-fluid">
    @Html.ActionLink("ANA SAYFA", "Index", "Default",
   new { },
   new { @class = "navbar-brand" })
</div>
</center>
</html>

using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

public class HomeController : Controller
{
    [HttpGet]
    public ActionResult Index()
    {
        return View();
    }

    [HttpPost]
    public ActionResult Index(int sayi1, int sayi2)
    {
        ViewBag.Sayi1 = sayi1;
        ViewBag.Sayi2 = sayi2;
        ViewBag.Toplam = sayi1 + sayi2;
        return View();
    }
}

using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Movies.Models
{
    public class Movie
    {
        public int Id { get; set; }

        [Display(Name = "ชื่อภาพยนต์"), StringLength(60, MinimumLength = 3)]
        [Required]
        public string Title { get; set; }

        [Display(Name = "วันฉายภาพยนต์"), DataType(DataType.Date)]
        public DateTime ReleaseDate { get; set; }

        [Display(Name = "ประเภทภาพยนต์"),RegularExpression(@"^[A-Z]+[a-zA-Z]*$"),Required,StringLength(30)]
        public string Genre { get; set; }

        [Display(Name = "ราคา"),DataType(DataType.Currency),Range(1, 100)]
        [Column(TypeName = "decimal(18,2")]
        public decimal Price { get; set; }

        [Display(Name = "คะแนนภาพยนต์"),RegularExpression(@"^[A-Z]+[a-zA-Z]*$"),Required]
        public string Rating { get; set; }
    }
}
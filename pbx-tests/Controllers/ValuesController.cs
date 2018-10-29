using System.Collections.Generic;
using System.Linq;
using Microsoft.AspNetCore.Mvc;

namespace pbx_tests.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ValuesController : ControllerBase
    {
        private readonly List<Value> _values = new List<Value>
        {
            new Value
            {
                Id = 1,
                Title = "value1",
                Important = false
            },
            new Value
            {
                Id = 2,
                Title = "value2",
                Important = true
            }
        };

        // GET api/values
        [HttpGet]
        public ActionResult<IEnumerable<Value>> Get()
        {
            return _values;
        }

        // GET api/values/1
        [HttpGet("{id}")]
        public ActionResult<Value> Get(int id)
        {
            return _values.FirstOrDefault(x=>x.Id == id);
        }

        // POST api/values
        [HttpPost]
        public void Post([FromBody] Value value)
        {
            value.Id = _values.Count;
            _values.Add(value);
        }

        // PUT api/values/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] Value value)
        {
            if (!_values.Exists(x => x.Id == id))
            {
                return;
            }

            _values[id] = value;
        }

        // DELETE api/values/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
            if (!_values.Exists(x => x.Id == id))
            {
                return;
            }

            _values.Remove(_values.FirstOrDefault(x => x.Id == id));
        }
    }
}
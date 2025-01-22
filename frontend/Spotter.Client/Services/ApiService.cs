using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Spotter.Client.Services
{
    public class ApiService
    {
        private readonly HttpClient _httpClient;

        public ApiService(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        // API hívás a Flask backendhez
        public async Task<string> GetApiData()
        {
            try {
                var response = await _httpClient.GetStringAsync("http://127.0.0.1:5001/api/data");
                return response;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
                return null;
            }
        }
    }
}

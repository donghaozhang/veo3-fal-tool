#!/usr/bin/env python3
"""
Test script to verify MCP server functionality.
This tests the MCP protocol communication without running the full server.
"""

import asyncio
import json
import sys
from mcp_server import server, format_cost_warning, format_model_info, format_generation_result

async def test_mcp_tools():
    """Test MCP server tools functionality"""
    print("🧪 Testing MCP Server Tools...")
    
    try:
        # Test 1: List models tool
        print("\n1️⃣ Testing list_models tool...")
        from mcp_server import handle_list_tools
        result = await handle_list_tools()
        tools = [tool.name for tool in result]
        expected_tools = [
            "generate_image",
            "batch_generate_images", 
            "list_models",
            "get_model_info",
            "download_image"
        ]
        
        for tool in expected_tools:
            if tool in tools:
                print(f"   ✅ Tool '{tool}' found")
            else:
                print(f"   ❌ Tool '{tool}' missing")
                return False
        
        # Test 2: Test formatting functions
        print("\n2️⃣ Testing formatting functions...")
        
        # Test cost warning
        cost_warning = format_cost_warning(0.015, 1)
        if "💰" in cost_warning and "0.015" in cost_warning:
            print("   ✅ Cost warning format works")
        else:
            print("   ❌ Cost warning format failed")
            return False
        
        # Test model info
        model_info = format_model_info("imagen4")
        if "imagen4" in model_info and "Endpoint:" in model_info:
            print("   ✅ Model info format works")
        else:
            print("   ❌ Model info format failed")
            return False
        
        # Test generation result
        mock_result = {
            'success': True,
            'image_url': 'https://example.com/image.png',
            'model': 'imagen4',
            'generation_time': 5.0
        }
        result_text = format_generation_result(mock_result)
        if "Generation Successful" in result_text and "5.0" in result_text:
            print("   ✅ Generation result format works")
        else:
            print("   ❌ Generation result format failed")
            return False
        
        print("\n✅ All MCP functionality tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ MCP functionality test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_generator_integration():
    """Test FAL generator integration"""
    print("\n🔗 Testing FAL Generator Integration...")
    
    try:
        from fal_text_to_image_generator import FALTextToImageGenerator
        
        # Test generator initialization
        generator = FALTextToImageGenerator()
        print("   ✅ Generator initialization successful")
        
        # Test generator methods
        print("   🔧 Testing generator methods...")
        if hasattr(generator, 'generate_image'):
            print("   ✅ generate_image method available")
        if hasattr(generator, 'batch_generate'):
            print("   ✅ batch_generate method available")
        if hasattr(generator, 'get_model_info'):
            print("   ✅ get_model_info method available")
        
        print("\n✅ Generator integration tests completed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Generator integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_mcp_config():
    """Test MCP configuration file"""
    print("\n⚙️ Testing MCP Configuration...")
    
    try:
        import json
        with open('mcp_config.json', 'r') as f:
            config = json.load(f)
        
        # Check required fields
        if 'mcpServers' in config:
            print("   ✅ MCP servers configuration found")
        else:
            print("   ❌ MCP servers configuration missing")
            return False
        
        if 'fal-text-to-image' in config['mcpServers']:
            print("   ✅ FAL text-to-image server configuration found")
        else:
            print("   ❌ FAL text-to-image server configuration missing")
            return False
        
        server_config = config['mcpServers']['fal-text-to-image']
        if 'command' in server_config and 'args' in server_config:
            print("   ✅ Server command and args configured")
        else:
            print("   ❌ Server command or args missing")
            return False
        
        print("\n✅ MCP configuration tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ MCP configuration test failed: {e}")
        return False

async def main():
    """Run all tests"""
    print("🚀 Starting MCP Server Comprehensive Tests...\n")
    
    # Test 1: MCP Configuration
    config_ok = test_mcp_config()
    
    # Test 2: MCP Tools Functionality  
    tools_ok = await test_mcp_tools()
    
    # Test 3: Generator Integration
    generator_ok = await test_generator_integration()
    
    # Summary
    print("\n" + "="*50)
    print("📊 TEST SUMMARY:")
    print(f"   MCP Configuration: {'✅ PASS' if config_ok else '❌ FAIL'}")
    print(f"   MCP Tools: {'✅ PASS' if tools_ok else '❌ FAIL'}")
    print(f"   Generator Integration: {'✅ PASS' if generator_ok else '❌ FAIL'}")
    
    all_passed = config_ok and tools_ok and generator_ok
    print(f"\n🎯 Overall Result: {'✅ ALL TESTS PASSED' if all_passed else '❌ SOME TESTS FAILED'}")
    
    if all_passed:
        print("\n🎉 MCP server is ready for use!")
        print("   You can now integrate it with Claude Desktop or other MCP clients.")
    else:
        print("\n🔧 Please fix the failing tests before using the MCP server.")
    
    return all_passed

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1) 
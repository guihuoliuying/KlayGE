// RenderView.cpp
// KlayGE 渲染视图类 实现文件
// Ver 3.3.0
// 版权所有(C) 龚敏敏, 2006
// Homepage: http://www.klayge.org
//
// 3.3.0
// 初次建立 (2006.5.31)
//
// 修改记录
//////////////////////////////////////////////////////////////////////////////////

#include <KlayGE/KlayGE.hpp>
#include <KFL/Util.hpp>
#include <KlayGE/RenderView.hpp>

namespace KlayGE
{
	void RenderView::OnBind(FrameBuffer& /*fb*/, uint32_t /*att*/)
	{
	}
	
	void RenderView::OnUnbind(FrameBuffer& /*fb*/, uint32_t /*att*/)
	{
	}


	void UnorderedAccessView::OnBind(FrameBuffer& /*fb*/, uint32_t /*att*/)
	{
	}
	
	void UnorderedAccessView::OnUnbind(FrameBuffer& /*fb*/, uint32_t /*att*/)
	{
	}
}
